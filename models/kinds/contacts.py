from models.kinds import base

from google.appengine.ext import ndb


class ContactUs(base.Base):
    """Models an interested individual."""
    firstname = ndb.StringProperty(required=True)
    lastname = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    phone_number = ndb.StringProperty()
    comment = ndb.StringProperty()
