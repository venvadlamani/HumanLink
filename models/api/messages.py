import services.asserts as asserts
from models.kinds.messages import (Thread, Message)
from models.dto.messages import (ThreadDto, MessageDto)
from models.api.base import BaseApiModel
from models.api.accounts import UserApiModel

from google.appengine.ext import ndb


class ThreadApiModel(BaseApiModel):
    """Represents thread details."""
    id = ndb.IntegerProperty()
    updated = Thread.updated
    subject = Thread.subject
    members = ndb.StructuredProperty(UserApiModel, repeated=True)
    unread_count = ndb.IntegerProperty()
    preview = ndb.StringProperty()

    @classmethod
    def from_thread_dto(cls, thread_dto):
        """Translates the given ThreadDto to an ThreadApiModel.

        :param thread_dto: (dto.messages.ThreadDto)
        :return: (api.messages.ThreadApiModel)
        """
        asserts.type_of(thread_dto, ThreadDto)

        member_models = [UserApiModel.from_user_dto(m)
                         for m in thread_dto.members]
        thread_api = ThreadApiModel(
            id=thread_dto.id,
            updated=thread_dto.updated,
            unread_count=thread_dto.unread_count,
            members=member_models,
            subject=thread_dto.subject,
            preview=thread_dto.preview,
        )
        return thread_api.ToMessage()


class MessageApiModel(BaseApiModel):
    """Represents a message that belongs to a thread."""
    id = ndb.IntegerProperty()
    thread_id = ndb.IntegerProperty()
    created = Message.created
    text = Message.text
    message_type = Message.message_type
    sender = ndb.StructuredProperty(UserApiModel)

    @classmethod
    def from_message_dto(cls, message_dto):
        """Translates the given MessageDto to a MessageApiModel.

        :param message_dto: (dto.messages.MessageDto)
        :return (api.messages.MessageApiModel)
        """
        asserts.type_of(message_dto, MessageDto)

        message_api = MessageApiModel(
            id=message_dto.id,
            thread_id=message_dto.thread_id,
            created=message_dto.created,
            text=message_dto.text,
            sender=UserApiModel.from_user_dto(message_dto.sender),
        )
        return message_api.ToMessage()


class NewThreadRequest(BaseApiModel):
    """New thread request model."""
    recipients = ndb.IntegerProperty(repeated=True)
    text = ndb.StringProperty()
    subject = ndb.StringProperty()
