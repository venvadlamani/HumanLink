"""These structs are typically enums or structured properties. They should not
be stored in the datastore. They should used from ndb models that
are stored in the datastore."""

from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext.ndb import msgprop
from google.appengine.ext import ndb
from protorpc import messages


class AccountType(messages.Enum):
    Caregiver = 0
    Careseeker = 1
    Professional = 2
    CommunityLeader = 3


class Country(messages.Enum):
    US = 0


class State(messages.Enum):
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
    Other = 0
    Female = 1
    Male = 2


class Language(messages.Enum):
    English = 0
    Arabic = 1
    French = 2
    Gujarati = 3
    Hindi = 4
    Polish = 5
    Portuguese = 6
    Russian = 7
    Spanish = 8
    Tagalog = 9
    Tamil = 10
    Telugu = 11
    Urdu = 12
    Vietnamese = 13


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
    Companion = 0
    Personal = 1
    AlzheimerDimentia = 2


class Address(EndpointsModel):
    type = ndb.StringProperty()
    street1 = ndb.StringProperty()
    street2 = ndb.StringProperty()
    city = ndb.StringProperty()
    state = msgprop.EnumProperty(State)
    zipcode = ndb.IntegerProperty()
    country = msgprop.EnumProperty(Country, default=Country.US)


class License(EndpointsModel):
    """A license that a caregiver has."""
    name = ndb.StringProperty(required=True)
    state = msgprop.EnumProperty(State)
    number = ndb.StringProperty()
    date = ndb.DateProperty(indexed=False)


class Certification(EndpointsModel):
    """A certification that a caregiver has."""
    name = ndb.StringProperty(required=True)
    state = msgprop.EnumProperty(State)
    date = ndb.DateProperty(indexed=False)


class WorkExperience(EndpointsModel):
    employer = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=True)
    phone_number = ndb.IntegerProperty()
    job_description = ndb.TextProperty()
    start_date = ndb.DateProperty()
    end_date = ndb.DateProperty()


class Allergy(messages.Enum):
    """Allergies."""
    Cats = 0
    Dogs = 1
    Smoking = 2


class Transportation(messages.Enum):
    """Transportation options."""
    CanProvide = 0
    CanDrive = 1
    NotDrive = 2