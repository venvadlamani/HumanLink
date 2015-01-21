import services.exp as exp
import services.messages
from controllers.api.base import (
    handle_exception,
    humanlink_api,
    get_current_user,
    user_required,
)
from models.api.messages import (
    ThreadApiModel,
    MessageApiModel,
    NewThreadRequest,
)
from models.api.base import (SimpleRequest, SimpleResponse)

from protorpc import remote


@humanlink_api.api_class(resource_name='messages', path='messages')
class MessagesApi(remote.Service):

    @SimpleRequest.method(name='inbox', path='inbox', http_method='GET',
                          request_fields=(),
                          response_message=ThreadApiModel.ProtoCollection())
    @user_required
    def inbox(self, req):
        """Retrieve the account's inbox."""
        try:
            account = get_current_user()
            thread_dtos = services.messages.threads(account.id)
            api_models = [ThreadApiModel.from_thread_dto(thd)
                          for thd in thread_dtos]
            return ThreadApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='thread', path='{thread_id}', http_method='GET',
                          request_fields=('thread_id',),
                          response_message=MessageApiModel.ProtoCollection())
    @user_required
    def thread(self, req):
        """Retrieve messages in a thread.

        :param req.thread_id: (int) ID of the thread.
        """
        thread_id = req.thread_id
        try:
            account = get_current_user()
            msg_dtos = services.messages.messages(account.id, thread_id)
            api_models = [MessageApiModel.from_message_dto(msg)
                          for msg in msg_dtos]
            return MessageApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @NewThreadRequest.method(name='new', path='new', http_method='POST',
                             response_message=ThreadApiModel.ProtoModel())
    @user_required
    def new_thread(self, req):
        """Create a new thread."""
        recipients, text = req.recipients, req.text
        try:
            account = get_current_user()
            thread_dto = services.messages.create_thread(account.id,
                                                         recipients, text)
            api_model = ThreadApiModel.from_thread_dto(thread_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @MessageApiModel.method(name='send', path='send', http_method='POST',
                            request_fields=('thread_id', 'text'),
                            response_message=MessageApiModel.ProtoModel())
    @user_required
    def send(self, req):
        """Send a reply in a thread.

        :param req.thread_id: (int) ID of the thread.
        :param req.text: (str) message to send.
        """
        thread_id, text = req.thread_id, req.text
        try:
            account = get_current_user()
            msg_dto = services.messages.send(account.id, thread_id, text)
            api_model = MessageApiModel.from_message_dto(msg_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='leave', path='leave', http_method='POST',
                          request_fields=('thread_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def leave(self, req):
        """Leave a thread.

        :param req.thread_id: (int) ID of the thread.
        """
        resp = SimpleResponse()
        thread_id = req.thread_id
        try:
            account = get_current_user()
            services.messages.leave_thread(account.id, thread_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='hide', path='hide', http_method='POST',
                          request_fields=('message_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def hide(self, req):
        """Hide a message in a thread.

        :param req.message_id: (int) ID of the message to hide.
        """
        resp = SimpleResponse()
        message_id = req.message_id
        try:
            account = get_current_user()
            services.messages.hide_message(account.id, message_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)
