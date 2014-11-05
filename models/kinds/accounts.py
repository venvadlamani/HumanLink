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


class AccountType(messages.Enum):
    PERSON = 0
    BUSINESS = 1


class Country(messages.Enum):
    US = 0


class State(messages.Enum):
    """ What about states of other countries?"""
    AL = 0
    AK = 1
    AR = 2
    AZ = 3
    CA = 4
    CO = 5
    CT = 6
    DE = 7
    FL = 8
    GA = 9
    HI = 10
    IA = 11
    ID = 12
    IL = 13
    IN = 14
    KS = 15
    KY = 16
    LA = 17
    MA = 18
    MD = 19
    ME = 20
    MI = 21
    MN = 22
    MO = 23
    MS = 24
    MT = 25
    NC = 26
    ND = 27
    NE = 28
    NH = 29
    NJ = 30
    NM = 31
    NV = 32
    NY = 33
    OH = 34
    OK = 35
    OR = 36
    PA = 37
    RI = 38
    SC = 39
    SD = 40
    TN = 41
    TX = 42
    UT = 43
    VA = 44
    VT = 45
    WA = 46
    WI = 47
    WV = 48
    WY = 49


class Gender(messages.Enum):
    MALE = 0
    FEMALE = 1


class Language(messages.Enum):
    ENGLISH = 0
    SPANISH = 1
    FRENCH = 2
    PORTUGUESE = 3
    GUJARATI = 4
    HINDI = 5
    TAMIL = 6
    TELUGU = 7
    POLISH = 8
    RUSSIAN = 9
    ARABIC = 10
    URDU = 11
    TAGALOG = 12
    VIETNAMESE = 13


class Expertise(messages.Enum):
    ALS = 0
    AlzheimersDisease = 1
    BloodDisorders = 2
    Cancer = 3
    CardiovascularDisease = 4
    Dementia = 5
    Diabetes = 6
    Hospice = 7
    MultipleSchlerosis = 8
    NeurologicalDisorders = 9
    OrthopedicCare = 10
    ParkinsonsDisease = 11
    PostSurgeryRecovery = 12
    RespiratoryDisorders = 13


class CareService(messages.Enum):
    BathingDressingGrooming = 0
    Companionship = 1
    EatingAssistance = 2
    GastrointestinalCare = 3
    LightHousekeeping = 4
    MealPreparation = 5
    MedicationManagement = 6
    MobilityAssistance = 7
    ToiletingAndIncontinence = 8
    Transportation = 9


class Address(ndb.Model):
    """ Type to represent Home, Work or any alternate address """
    type = ndb.StringProperty()
    street1 = ndb.StringProperty(required=True)
    street2 = ndb.StringProperty()
    city = ndb.StringProperty(required=True)
    state = msgprop.EnumProperty(State, required=True)
    zipcode = ndb.IntegerProperty(required=True)
    country = ndb.StringProperty(default='US', required=True)


class License(ndb.Model):
    """ The licenses that the caregiver has """
    name = ndb.StringProperty(required=True)
    state = msgprop.EnumProperty(State)
    date = ndb.DateProperty(required=True)


class Certification(ndb.Model):
    """ The certifications that the caregiver has """
    name = ndb.StringProperty(required=True)
    state = msgprop.EnumProperty(State)
    date = ndb.DateProperty(required=True)


class WorkExperience(ndb.Model):
    """ Work experience for the caregivers """
    employer = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=True)
    phone_number = ndb.IntegerProperty(required=True)
    job_description = ndb.StringProperty(required=True)
    start_date = ndb.DateProperty(required=True)
    end_date = ndb.DateProperty()


class PaymentInfo(ndb.Model):
    """ Person specific stripe token information """
    stripe_token = ndb.StringProperty(required=True)


class Caregiver(ndb.Model):
    """Caregiver specific details.

    TODO(murali): Figure out how to set computed property
    TODO(murali): Add photo property
    TODO(murali): Figure out how to model availability
    """
    gender = msgprop.EnumProperty(Gender, required=True)
    # Used to calculate age
    dob = ndb.DateProperty(required=True)
    # cg_age = ndb.ComputedProperty()
    bio = ndb.TextProperty()
    # Caregiver photo to be added
    languages = msgprop.EnumProperty(Language, repeated=True)
    licenses = ndb.StructuredProperty(License, repeated=True)
    work_experience = ndb.StructuredProperty(WorkExperience, repeated=True)
    certifications = ndb.StructuredProperty(Certification, repeated=True)
    careservices = ndb.StructuredProperty(CareService, repeated=True)


class Carerecipient(ndb.Model):
    """Carerecipient specific details.

    TODO(murali): Figure out how to set compute property for age
    """
    first = ndb.StringProperty(required=True)
    last = ndb.StringProperty(required=True)
    dob = ndb.DateProperty(required=True)
    # cr_age = ndb.ComputedProperty()
    gender = msgprop.EnumProperty(Gender, required=True)
    needs = ndb.TextProperty()
    address = ndb.StructuredProperty(Address, required=True)


class Account(base.Base, auth_models.User):
    """Account associated with an email address.
    This model expands the webapp2 user model used for authentication."""

    # Email address associated with the account (unique).
    email = ndb.StringProperty(required=True)
    # Facebook ID associated with the account.
    fbid = ndb.StringProperty()
    # Whether the account has been verified or not.
    verified = ndb.BooleanProperty(default=False)
    # Whether the account is for a Business or a Person
    account_type = msgprop.EnumProperty(AccountType)
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
    address = ndb.StructuredProperty(Address, repeated=True)
    caregiver = ndb.StructuredProperty(Caregiver)
    carerecipients = ndb.StructuredProperty(Carerecipient, repeated=True)
    payment_info = ndb.StructuredProperty(PaymentInfo)
    soft_delete = ndb.BooleanProperty(default=False)


class Business(base.Base):
    """Business specific details.

    TODO(murali): Add a photo
    """
    # Business account owner
    account_id = ndb.IntegerProperty()
    # Name of the business
    name = ndb.StringProperty(required=True)
    url = ndb.StringProperty()
    phone_number = ndb.IntegerProperty()
    about = ndb.TextProperty()
    address = ndb.StructuredProperty(Address)
