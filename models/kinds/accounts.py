import configs

import hashlib
import logging
import webapp2_extras.appengine.auth.models as auth_models

from models.kinds import base

from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc import messages


class ProfileType(messages.Enum):
    CAREGIVER = 0
    CARESEEKER = 1


class Caregiver(ndb.Model):
    """Caregiver specific details."""
    caregiver_details = ndb.StringProperty()


class Careseeker(ndb.Model):
    """Careseeker specific details."""
    careseeker_details = ndb.StringProperty()


class Account(base.Base, auth_models.User):
    """Account associated with an email address.
    This model expands the webapp2 user model used for authentication."""

    # Email address associated with the account (unique).
    email = ndb.StringProperty(required=True)
    # Facebook ID associated with the account.
    fbid = ndb.StringProperty()
    # Whether the account has been verified or not.
    verified = ndb.BooleanProperty(default=False)
    # Whether the account is soft deleted.
    soft_delete = ndb.BooleanProperty(default=False)

    @property
    def verification_token(self):
        """Returns the email verification token for this account."""
        if not self.email:
            logging.error('Email does not exist.')
            return
        return hashlib.md5(
            (configs.VERIF_SECRET + self.email).encode('utf-8')).hexdigest()


class Profile(base.Base):
    """Profile."""

    # Account owner of the profile.
    account_id = ndb.IntegerProperty()
    # First and last name.
    first = ndb.StringProperty()
    last = ndb.StringProperty()
    # Profile types. Not indexed by default.
    profile_types = msgprop.EnumProperty(ProfileType, repeated=True)
    # Phone number.
    # Eventually switch to this:
    #   https://github.com/daviddrysdale/python-phonenumbers
    phone_number = ndb.IntegerProperty()
    caregiver = ndb.StructuredProperty(Caregiver)
    careseeker = ndb.StructuredProperty(Careseeker)
    soft_delete = ndb.BooleanProperty(default=False)
