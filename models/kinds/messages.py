from models.kinds import base

from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc import messages


class MessageType(messages.Enum):
    """A message is either user-generated or system-generated."""
    User = 0
    System = 1


class Member(base.Base, EndpointsModel):
    """Thread member.

    NOTE: Don't persist this; instead, use in messages.Thread.
    """
    account_id = ndb.IntegerProperty(required=True)
    hidden = ndb.BooleanProperty(default=False)
    last_seen = ndb.DateTimeProperty(indexed=False)


class Thread(base.Base):
    """Thread details."""
    members = ndb.StructuredProperty(Member, repeated=True)
    subject = ndb.StringProperty(indexed=False)
    last_message_id = ndb.IntegerProperty(indexed=False)

    def add_member(self, account_id):
        """Add a new member to the list of thread members.

        NOTE: Does nto persist.

        :param account_id: (int) ID of an account to add.
        :return: (None)
        """
        self.members.append(Member(account_id=account_id))

    def find_member(self, account_id):
        """Find a member by account_id.

        :param account_id: (int) ID of the member's account.
        :return: (kinds.messages.Member)
        """
        for member in self.members:
            if member.account_id == account_id:
                return member


class Message(base.Base):
    """Message that belongs to a thread."""
    thread_id = ndb.IntegerProperty(required=True)
    sender_id = ndb.IntegerProperty(indexed=False)
    text = ndb.TextProperty(indexed=False)
    message_type = msgprop.EnumProperty(
        MessageType, default=MessageType.User, indexed=False)
    # List of accounts who hid this message.
    hidden_member_ids = ndb.IntegerProperty(repeated=True)
    # messages.MessageAttachment IDs
    attachment_ids = ndb.IntegerProperty(repeated=True, indexed=False)


class MessageAttachment(base.Base):
    """Attachment that belongs to a message.

    NOTE: Non-functional at the moment.
    """
    message_id = ndb.IntegerProperty(required=True, indexed=False)
