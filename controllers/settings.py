from controllers import base
from models.kinds.settings import Notifications
import logging


class Settings(base.BaseHandler):
    """Settings related controller."""

    def index(self):
        """Index page."""
        self.render('settings/index.html')

    def POST_settings_notifications(self):
        """Notifications POST request."""
        ntfn = Notifications.query(account_id==self.request_json.get('account_id'))
        ntfn.email_promotions = self.request_json.get('email_promotions')
        ntfn.email_updates = self.request_json.get('email_updates')
        ntfn.sms_account_changes = self.request_json.get('sms_account_changes')
        ntfn.sms_from_user = self.request_json.get('sms_from_user')
        ntfn.put()

        self.write_json({'message': 'Successful.'})

    def GET_settings_notifications(self):
        """Notifications GET request."""
        account_id = self.request.get('account_id')
        qry = Notifications.query(Notifications.account_id == str(account_id)).fetch()
        notifications_map = {}

        for row in qry:
            notifications_map = {
                'email_promotions': row.email_promotions,
                'email_updates': row.email_updates,
                'sms_account_changes': row.sms_account_changes,
                'sms_from_user': row.sms_from_user,
            }

        self.write_json(notifications_map)
