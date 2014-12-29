import services.accounts
import services.connections
import services.exp as exp
from controllers.api.base import (
    handle_exception,
    humanlink_api,
    get_current_user,
    user_required
)
from models.api.base import (SimpleRequest, SimpleResponse)
from models.api.connections import (PendingConnApiModel, ConnApiModel)

from protorpc import remote


@humanlink_api.api_class(resource_name='connections', path='connections')
class ConnectionsApi(remote.Service):

    @SimpleRequest.method(name='request', path='request', http_method='POST',
                          request_fields=('account_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def request(self, req):
        """Send a connection request to a user.

        :param req.account_id: (int) ID of the account receiving the request.
        """
        resp = SimpleResponse()
        to_id = req.account_id
        try:
            account = get_current_user()
            services.connections.send_request(account.id, to_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='accept', path='accept', http_method='POST',
                          request_fields=('account_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def accept(self, req):
        """Accept a connection request from a user.

        :param req.account_id: (int)
            ID of the account that sent the connection request.
        """
        resp = SimpleResponse()
        from_id = req.account_id
        try:
            account = get_current_user()
            services.connections.accept_request(account.id, from_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='decline', path='decline', http_method='POST',
                          request_fields=('account_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def decline(self, req):
        """Decline a connection request form a user.

        :param req.account_id: (int)
            ID of the account that sent the connection request.
        """
        resp = SimpleResponse()
        from_id = req.account_id
        try:
            account = get_current_user()
            services.connections.decline_request(account.id, from_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='remove', path='remove', http_method='POST',
                          request_fields=('account_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def remove(self, req):
        """Remove an existing connection.

        :param req.account_id: (int) ID of the account to be removed.
        """
        resp = SimpleResponse()
        other_id = req.account_id
        try:
            account = get_current_user()
            services.connections.remove_connection(account.id, other_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='my', path='my', http_method='GET',
                          request_fields=(),
                          response_message=ConnApiModel.ProtoCollection())
    @user_required
    def my(self, req):
        """Retrieve the current account's connections."""
        try:
            account = get_current_user()
            dtos = services.connections.my_connections(account.id)
            print(dtos)
            api_models = [ConnApiModel.from_conn_dto(d) for d in dtos]
            return ConnApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='pending', path='pending', http_method='GET',
                          request_fields=(),
                          response_message=PendingConnApiModel.ProtoCollection())
    @user_required
    def pending(self, req):
        """Retrieve the current account's pending connections requests."""
        try:
            account = get_current_user()
            dtos = services.connections.pending_requests(account.id)
            api_models = [PendingConnApiModel.from_conn_dto(d) for d in dtos]
            return PendingConnApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)
