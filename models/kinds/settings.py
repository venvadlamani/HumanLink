from models.kinds import base
from google.appengine.ext import ndb

class Payment(base.Base):
    """Payment information. Currently supports only Stripe."""
    account_id = ndb.IntegerProperty(required=True)
    payment_plan = ndb.StringProperty()
    stripe_token = ndb.StringProperty(indexed=False)
