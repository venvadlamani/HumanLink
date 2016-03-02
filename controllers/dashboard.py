from google.appengine.ext import ndb
from controllers import base
from models.kinds.accounts import Account


class Dashboard(base.BaseHandler):
    def index(self):
        self.render('dashboard/index.html')
