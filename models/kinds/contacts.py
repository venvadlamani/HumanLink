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
