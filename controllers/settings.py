from controllers import base
from models.kinds.settings import Notifications
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
        results = Notifications.query(Notifications.account_id == accountid)

        for row in results:
            new_ntfn = row.key.get()
            new_ntfn.account_id = str(self.request_json.get('account_id'))
            new_ntfn.email_promotions = self.request_json.get('email_promotions')
            new_ntfn.email_updates = self.request_json.get('email_updates')
            new_ntfn.put()
