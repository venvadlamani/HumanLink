from controllers import base
from models.kinds.settings import Notifications
from models.kinds.settings import Payments
from models.kinds.accounts import Account
from webapp2_extras import security

from google.appengine.ext import ndb


class Settings(base.BaseHandler):
    """Settings related controller."""

    def index(self):
        """Index page."""
        self.render('settings/index.html')

    def GET_notifications(self):
        """Notifications GET request."""
        notifications_map = {}
        account_id = self.request.get('account_id')
        qry = Notifications.query(Notifications.account_id == str(account_id)).fetch()

        if len(qry) == 0:
            ntfn = Notifications()
            ntfn.account_id = str(self.request.get('account_id'))
            ntfn.put()

        if len(qry) > 0:
            for row in qry:
                notifications_map = {
                    'email_promotions': row.email_promotions,
                    'email_updates': row.email_updates,
                }

        self.write_json(notifications_map)

    def POST_notifications(self):
        """Notifications update POST request."""
        accountid = self.request_json.get('account_id')
        qry = Notifications.query(Notifications.account_id == accountid)

        for row in qry:
            new_ntfn = row.key.get()
            new_ntfn.account_id = str(self.request_json.get('account_id'))
            new_ntfn.email_promotions = self.request_json.get('email_promotions')
            new_ntfn.email_updates = self.request_json.get('email_updates')
            new_ntfn.put()

    def GET_payments(self):
        """Payments GET request."""
        payments_map = {}
        account_id = self.request.get('account_id')
        qry = Payments.query(Payments.account_id == str(account_id)).fetch()

        if len(qry) == 0:
            pymt = Payments()
            pymt.account_id = str(self.request.get('account_id'))
            pymt.put()

        if len(qry) > 0:
            for row in qry:
                payments_map = {
                    'payment_plan': row.payment_plan,
                    'card_number': row.card_number,
                    'expiry_month': row.expiry_month,
                    'expiry_year': row.expiry_year,
                    'stripe_token': row.stripe_token,
                }

        self.write_json(payments_map)

    def POST_payments(self):
        """Payments update POST request."""
        accountid = self.request_json.get('account_id')
        qry = Payments.query(Payments.account_id == accountid)

        for row in qry:
            new_pymt = row.key.get()
            new_pymt.card_number = self.request_json.get('card_number')
            new_pymt.expiry_month = self.request_json.get('expiry_month')
            new_pymt.expiry_year = self.request_json.get('expiry_year')
            new_pymt.payment_plan = self.request_json.get('payment_plan')
            new_pymt.stripe_token = self.request_json.get('stripe_token')
            new_pymt.put()

    def POST_security(self):
        """Security update POST request."""
        email = self.request_json.get('email')
        qry = Account.query(Account.email == email)

        for row in qry:
            acct = row.key.get()
            acct.password = security.generate_password_hash(
                self.request_json.get('password'), length=12)
            acct.put()
