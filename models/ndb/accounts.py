from models.ndb import base
import webapp2_extras.appengine.auth.models as auth_models

from google.appengine.ext import ndb


class Account(base.Base, auth_models.User):
    """Account associated with an email address.
    This model expands the webapp2 user model used for authentication."""
    email = ndb.StringProperty(required=True)
    # This is a placeholder.
    name = ndb.StringProperty()
    verified = ndb.BooleanProperty(default=False)
    soft_delete = ndb.BooleanProperty(default=False)


class Profile(base.Base):
    """Profile."""
    owner = ndb.KeyProperty(kind=Account)
    first = ndb.StringProperty()
    last = ndb.StringProperty()
    address = ndb.StringProperty()

    @classmethod
    def delete_profiles(cls, account_id):
        """Deletes the profiles associated with the given account_id."""
        if not account_id:
            return
        profiles = cls.query(
            cls.owner == ndb.Key(Account, account_id)).fetch(keys_only=True)
        return ndb.delete_multi(profiles)
