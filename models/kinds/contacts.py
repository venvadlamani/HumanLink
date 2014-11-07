from models.kinds import base

from google.appengine.ext import ndb


class ContactUs(base.Base):
    """Models an interested individual."""
    first_name = ndb.StringProperty(required=True)
    last_name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
