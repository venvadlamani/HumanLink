import configs
from models.kinds import base
from models.kinds.structs import (
    AccountType,
    Address,
    Allergy,
    CareService,
    Certification,
    Expertise,
    Gender,
    Language,
    License,
    Transportation,
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
    first = ndb.StringProperty(indexed=False)
    last = ndb.StringProperty(indexed=False)
    names = ndb.ComputedProperty(
        lambda self: [self.first.lower(), self.last.lower()], repeated=True)
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
    account_id = ndb.IntegerProperty(required=True, indexed=False)
    care_services = msgprop.EnumProperty(CareService, repeated=True)
    zipcode = ndb.IntegerProperty()
    gender = msgprop.EnumProperty(Gender, indexed=True)
    dob = ndb.DateTimeProperty()
    headline = ndb.StringProperty(indexed=False)
    bio = ndb.TextProperty(indexed=False)
    languages = msgprop.EnumProperty(Language, repeated=True, indexed=True)
    licenses = ndb.StructuredProperty(License, repeated=True)
    certifications = ndb.StructuredProperty(Certification, repeated=True)
    expertise = msgprop.EnumProperty(Expertise, repeated=True, indexed=True)
    gender_preference = msgprop.EnumProperty(Gender, indexed=True)
    allergies = msgprop.EnumProperty(Allergy, repeated=True, indexed=True)
    transportation = msgprop.EnumProperty(
        Transportation, repeated=True, indexed=True)
    live_in = ndb.BooleanProperty(default=False)
    # TODO: Find out if work experience is actually needed.
    #work_experience = ndb.StructuredProperty(WorkExperience, repeated=True)


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
