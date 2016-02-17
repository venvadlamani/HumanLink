from models.kinds import base
from google.appengine.ext import ndb


class ContactUs(base.Base):
    """Models an interested individual."""
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    # Interest choices:
    #    1: interested in care giving
    #    2: interested in receiving care
    #    3: interested in community manager (this selection is not for MVP)
    interest = ndb.IntegerProperty(required=True, choices=[1, 2])
    zipcode = ndb.StringProperty()
    referrer = ndb.StringProperty()


class CaregiverGeneral(base.Base):
    """Models a caregiver who has not created an account."""
    #   Personal Data
    name = ndb.StringProperty(required=True)
    location = ndb.StringProperty(required=True)
    phone_number = ndb.StringProperty(required=True)
    photo = ndb.StringProperty()
    gender = ndb.StringProperty()
    live_in = ndb.BooleanProperty()

    # Professional Data
    school = ndb.StringProperty()
    lpn = ndb.BooleanProperty()
    cna = ndb.BooleanProperty()
    iha = ndb.BooleanProperty()
    hcs = ndb.BooleanProperty()
    ad = ndb.BooleanProperty()

    # Headline and Bio
    headline = ndb.StringProperty()
    bio = ndb.StringProperty()

    # Professional Preferences
    weekdays = ndb.BooleanProperty()
    weekends = ndb.BooleanProperty()


class Request(base.Base):
    """Models a request from Guest/User."""
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    message = ndb.StringProperty(required=True)
