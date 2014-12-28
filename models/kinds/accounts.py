import configs
from models.kinds import base
from models.kinds.structs import (
    AccountType,
    Address,
    Gender,
    Language,
    License,
    CareService,
    Certification,
    WorkExperience,
)

import hashlib
import webapp2_extras.appengine.auth.models as auth_models
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop


class Account(base.Base, auth_models.User):
    """Account associated with an email address.

    This model expands the webapp2 user model used for authentication.
    """
    # Email address associated with the account (unique).
    email = ndb.StringProperty(required=True)
    # Primary account type.
    account_type = msgprop.EnumProperty(AccountType)
    first = ndb.StringProperty()
    last = ndb.StringProperty()
    # Facebook ID associated with the account.
    fbid = ndb.StringProperty(indexed=False)
    # Whether the email has been verified or not.
    email_verified = ndb.BooleanProperty(default=False, indexed=False)
    # Whether the account is soft deleted.
    soft_delete = ndb.BooleanProperty(default=False, indexed=False)
    # Phone number. Eventually switch to this:
    #   https://github.com/daviddrysdale/python-phonenumbers
    phone_number = ndb.IntegerProperty()
    phone_number_verified = ndb.IntegerProperty(indexed=False)
    address = ndb.StructuredProperty(Address)
    # accounts.Caregiver ID.
    caregiver_id = ndb.IntegerProperty()
    # accounts.Patient IDs.
    patient_ids = ndb.IntegerProperty(repeated=True, indexed=False)
    # accounts.Payment ID.
    payment_id = ndb.IntegerProperty(indexed=False)
    # connections.ConnList ID.
    connlist_id = ndb.IntegerProperty(indexed=False)

    @property
    def verification_token(self):
        """Returns the email verification token for this account."""
        return hashlib.md5(
            (configs.VERIF_SECRET + self.email).encode('utf-8')).hexdigest()


class Caregiver(base.Base):
    """Caregiver specific details."""
    account_id = ndb.IntegerProperty(required=True)
    gender = msgprop.EnumProperty(Gender)
    dob = ndb.DateProperty()
    bio = ndb.TextProperty()
    languages = msgprop.EnumProperty(Language, repeated=True)
    licenses = ndb.StructuredProperty(License, repeated=True)
    work_experience = ndb.StructuredProperty(WorkExperience, repeated=True)
    certifications = ndb.StructuredProperty(Certification, repeated=True)
    careservices = msgprop.EnumProperty(CareService, repeated=True)


class Patient(base.Base):
    """Patient specific details."""
    account_id = ndb.IntegerProperty(required=True)
    first = ndb.StringProperty(indexed=False)
    last = ndb.StringProperty(indexed=False)
    phone_number = ndb.IntegerProperty(indexed=False)
    relationship = ndb.StringProperty(indexed=False)
    dob = ndb.DateProperty(indexed=False)
    gender = msgprop.EnumProperty(Gender, indexed=False)
    pets = ndb.StringProperty(repeated=True, indexed=False)
    care_type = msgprop.EnumProperty(CareService, repeated=True, indexed=False)
    caregiver_pref_gender = msgprop.EnumProperty(Gender, indexed=False)
    additional_info = ndb.TextProperty(indexed=False)
    address = ndb.StructuredProperty(Address, indexed=False)
    soft_delete = ndb.BooleanProperty(default=False, indexed=False)
    # accounts.Payment ID.
    payment_id = ndb.IntegerProperty(indexed=False)


class Payment(base.Base):
    """Payment information. Currently supports only Stripe."""
    account_id = ndb.IntegerProperty(required=True)
    stripe_token = ndb.StringProperty(indexed=False)
