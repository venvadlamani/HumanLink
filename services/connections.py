import services.accounts
import services.asserts as asserts
import services.exp as exp
from models.kinds.connections import (
    ConnList,
    ConnRequest,
    ConnStatus,
)
from models.dto.connections import (
    PendingDto,
    ConnDto,
)
import logging
from google.appengine.ext import ndb


def sent_requests(actor_id):
    """Retrieves sent requests.

    :param actor_id: (int) ID of the account.
    :return: (list<kinds.connections.ConnRequest>)
        A list of connection requests.
    """
    asserts.valid_id_type(actor_id)

    reqs = _conn_requests(from_id=actor_id, status=ConnStatus.Pending)
    return reqs


def pending_requests(actor_id):
    """Retrieves pending requests that were sent to an account.

    :param actor_id: (int) ID of the account.
    :return: (list<dto.connections.PendingDto>) A list of connection Dto's.
    """
    asserts.valid_id_type(actor_id)

    reqs = _conn_requests(to_id=actor_id, status=ConnStatus.Pending)
    account_ids = [r.from_id for r in reqs]
    accounts = services.accounts.accounts_by_ids(account_ids)

    return PendingDto.list_from_req_account(reqs, accounts)


def send_request(actor_id, to_id):
    """Sends a request from one account to another.

    TODO(kanat): Send email notification.

    :param actor_id: (int) ID of the account sending.
    :param to_id: (int) ID of the account receiving.
    :return: (kinds.connections.ConnRequest)
        Connection request that was created.
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(to_id)

    if actor_id == to_id:
        raise exp.BadRequestExp('Cannot send a request to self.')
    if not services.accounts.account_by_id(to_id):
        logging.warning('to_id={} does not exist.'.format(to_id))
        raise exp.NotFoundExp('Account does not exist.')
    # Maybe one or the other already sent a request.
    req = (_conn_request_get(from_id=actor_id, to_id=to_id)
           or _conn_request_get(from_id=to_id, to_id=actor_id))
    if req is not None:
        logging.info('Connection request already exists.')
        return
    req = ConnRequest(from_id=actor_id, to_id=to_id)
    req.put()
    return req


def accept_request(actor_id, from_id):
    """Accepts a connection request from the given account.

    TODO(kanat): Send email notification.

    :param actor_id: (int) ID of the account.
    :param from_id: (int) ID of the account that sent the connection request.
    :return: (kinds.connections.ConnRequest) Accepted connection request.
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(from_id)

    req = _conn_request_get(
        to_id=actor_id, from_id=from_id, status=ConnStatus.Pending)
    if req is None:
        logging.warning('Pending request does not exist: to={}, from={}'
                        .format(actor_id, from_id))
        raise exp.NotFoundExp('Request does not exist.')
    _accept_request(req)
    return req


def decline_request(actor_id, from_id):
    """Declines a connection request from the given account.

    :param actor_id: (int) ID of the account.
    :param from_id: (int) ID of the account that sent the connection request.
    :return: (None)
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(from_id)

    req = _conn_request_get(
        to_id=actor_id, from_id=from_id, status=ConnStatus.Pending)
    if req is None:
        logging.warning('Pending request does not exist: to={}, from={}'
                        .format(actor_id, from_id))
        raise exp.NotFoundExp('Request does not exist.')
    req.key.delete()


def my_connections(actor_id):
    """Returns the list of account IDs the account is connected to.

    :param actor_id: (int) ID of the account.
    :return: (list<dto.connections.ConnDto>) A list of account IDs.
    """
    asserts.valid_id_type(actor_id)

    connlist = _get_connlist(actor_id)
    reqs = ndb.get_multi(ConnRequest.ids_to_keys(connlist.accepted_reqs))
    accounts = services.accounts.accounts_by_ids(connlist.accepted_ids)

    return ConnDto.list_from_req_account(reqs, accounts)


def is_connected(first_id, second_id):
    """Check whether two accounts are connected.

    :param first_id: (int) ID of the first account.
    :param second_id: (int) ID of the second account.
    :return: (bool) True if connected; False otherwise.
    """
    asserts.valid_id_type(first_id)
    asserts.valid_id_type(second_id)

    connlist = _get_connlist(first_id)
    return second_id in connlist.accepted_ids


def remove_connection(actor_id, other_id):
    """Removes a connection from the account.

    :param actor_id: (int) ID of the account removing the connection.
    :param other_id: ID of the account to be removed.
    :return: (None)
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(other_id)

    if not is_connected(actor_id, other_id):
        logging.warning('Trying to remove a connection that doesn\'t exist: '
                        'actor={}, other={}'.format(actor_id, other_id))
        raise exp.NotFoundExp('Not connected.')

    connlistA = _get_connlist(actor_id)
    connlistB = _get_connlist(other_id)
    # Find the connection request.
    req = (_conn_request_get(from_id=actor_id, to_id=other_id)
           or _conn_request_get(from_id=other_id, to_id=actor_id))
    try:
        connlistA.accepted_reqs.remove(req.id)
        connlistB.accepted_reqs.remove(req.id)
    except ValueError:
        pass
    ndb.put_multi([connlistA, connlistB])
    req.key.delete()


def _conn_requests(from_id=None, to_id=None, status=None, fetch=True):
    """Fetches connection requests."""
    cls = ConnRequest
    query = cls.query()
    if from_id is not None:
        query = query.filter(cls.from_id == from_id)
    if to_id is not None:
        query = query.filter(cls.to_id == to_id)
    if status is not None:
        query = query.filter(cls.status == status)
    return query.fetch() if fetch else query.get()


def _conn_request_get(from_id=None, to_id=None, status=None):
    """Gets a connection request."""
    return _conn_requests(from_id, to_id, status, False)


def _accept_request(req):
    """Updates each others connections list.

    :return (None)
    """
    req.status = ConnStatus.Accepted
    req.put()

    connlistA = _get_connlist(req.from_id)
    connlistB = _get_connlist(req.to_id)

    connlistA.accepted_reqs.append(req.id)
    connlistB.accepted_reqs.append(req.id)

    ndb.put_multi([connlistA, connlistB])


def _get_connlist(account_id):
    """Returns the account's connections list.

    :return: (kinds.connections.ConnList)
    """
    account = services.accounts.account_by_id(account_id, _dto=False)
    return ConnList.get_by_id(account.connlist_id)
