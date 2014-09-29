import base

from google.appengine.api import users


class Accounts(base.BaseHandler):

    def signup(self):
        user = users.get_current_user()
        if user:
            templ = {'user': user}
            self.render('accounts/signup.html', templ)
        else:
            self.redirect(users.create_login_url('/login'))