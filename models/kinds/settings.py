from models.kinds import base
from google.appengine.ext import ndb


class Payments(base.Base):
    """Payment information. Currently supports only Stripe."""
    account_id = ndb.StringProperty(required=True)
    payment_plan = ndb.StringProperty()
    card_number = ndb.StringProperty()
    expiry_month = ndb.StringProperty()
    expiry_year = ndb.StringProperty()
    stripe_token = ndb.StringProperty(indexed=False)


class Notifications(base.Base):
    """Preferred notifications"""
    account_id = ndb.StringProperty(required=True)
    email_updates = ndb.BooleanProperty(default=False)
    email_promotions = ndb.BooleanProperty(default=False)
