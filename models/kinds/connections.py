from models.kinds import base

from google.appengine.ext.ndb import msgprop
from google.appengine.ext import ndb
from protorpc import messages


class ConnStatus(messages.Enum):
    """Connection request status."""
    Pending = 0
    Accepted = 1


class ConnRequest(base.Base):
    """Connection request.

    :key from_id: (int) ID of the account that sent the connection request.
    :key to_id: (int) ID of the account the request was sent to.
    :key status: (.ConnStatus) Status of the connection request.
    """
    from_id = ndb.IntegerProperty(required=True)
    to_id = ndb.IntegerProperty(required=True)
    message = ndb.TextProperty()
    status = msgprop.EnumProperty(ConnStatus, default=ConnStatus.Pending)


class ConnList(base.Base):
    """List of an account's accepted connections requests.

    :key account_id: ID the account this list belongs to.
    :key accepted_reqs: Accepted connection requests IDs.
    """
    account_id = ndb.IntegerProperty(required=True)
    accepted_reqs = ndb.IntegerProperty(repeated=True)

    @property
    def accepted_ids(self):
        """Returns account IDs of the account's accepted connections.

        :return: (list<int>)
        """
        reqs = ndb.get_multi(ConnRequest.ids_to_keys(self.accepted_reqs))
        return [r.from_id if r.to_id == self.account_id else r.to_id
                for r in reqs]
