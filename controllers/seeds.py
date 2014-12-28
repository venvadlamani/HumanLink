import services.accounts
import services.connections
from models.kinds.structs import AccountType

import logging


def seed():
    """Pre-populate the datastore with dummy entities.

    :return: (None)
    """
    _flush_datastore()

    # Create dummy accounts.
    ariana = create_ariana()
    peter = create_peter()
    jackie = create_jackie()
    kanat = create_kanat()
    ven = create_ven()
    justin = create_justin()

    # Connect them.
    # We don't follow the send_request -> accept_request flow
    # because of NDB's eventual consistency behavior.
    req = services.connections.send_request(ariana.id, peter.id)
    services.connections._accept_request(req)

    req = services.connections.send_request(ariana.id, jackie.id)
    services.connections._accept_request(req)

    req = services.connections.send_request(ariana.id, ven.id)
    services.connections._accept_request(req)

    req = services.connections.send_request(peter.id, jackie.id)
    services.connections._accept_request(req)

    req = services.connections.send_request(peter.id, justin.id)
    services.connections._accept_request(req)

    req = services.connections.send_request(jackie.id, kanat.id)
    services.connections._accept_request(req)

    req = services.connections.send_request(kanat.id, ven.id)
    services.connections._accept_request(req)

    req = services.connections.send_request(ven.id, justin.id)
    services.connections._accept_request(req)


def create_ariana():
    return _create_account('Ariana', 'A', AccountType.Caregiver)


def create_peter():
    return _create_account('Peter', 'B', AccountType.Caregiver)


def create_jackie():
    return _create_account('Jackie', 'C', AccountType.Professional)


def create_kanat():
    return _create_account('Kanat', 'D', AccountType.Careseeker)


def create_ven():
    return _create_account('Ven', 'E', AccountType.CommunityLeader)


def create_justin():
    return _create_account('Justin', 'F', AccountType.Careseeker)


def _create_account(first, last, account_type):
    account = services.accounts.create_account(
        first + '@humanlink.co', '123456', account_type, _dto=False)
    account.first = first
    account.last = last
    account.put()
    return account


def _flush_datastore():
    logging.warning('Please manually flush your datastore for now.')
