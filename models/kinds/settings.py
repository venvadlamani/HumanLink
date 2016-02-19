from models.kinds import base
from google.appengine.ext import ndb


class Payment(base.Base):
    """Payment information. Currently supports only Stripe."""
    account_id = ndb.IntegerProperty(required=True)
    payment_plan = ndb.StringProperty()
    stripe_token = ndb.StringProperty(indexed=False)


class Notifications(base.Base):
    """Preferred notifications"""
    account_id = ndb.StringProperty(required=True)
    sms_from_user = ndb.BooleanProperty()
    sms_account_changes = ndb.BooleanProperty()
    email_updates = ndb.BooleanProperty()
    email_promotions = ndb.BooleanProperty()
