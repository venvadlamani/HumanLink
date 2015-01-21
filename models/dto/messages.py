import services.asserts as asserts
from models.dto import map_props
from models.kinds.messages import Message


class MessageDto(object):

    _props = [
        'id', 'thread_id', 'sender', 'text', 'message_type', 'created',
    ]

    @classmethod
    def from_message_ndb(cls, message_ndb):
        """Translates the given Message to MessageDto.

        :param message_ndb: (kinds.messages.Message)
        :return: (dto.messages.MessageDto)
        """
        asserts.type_of(message_ndb, Message)

        message_dto = MessageDto()
        map_props(message_dto, message_ndb, MessageDto._props)
        return message_dto


class ThreadDto(object):

    _props = [
        'id', 'subject', 'members', 'updated', 'subject', 'preview',
        'unread_count',
    ]

    def __init__(self, **kwargs):
        for k in ThreadDto._props:
            if k in kwargs:
                setattr(self, k, kwargs.get(k))
