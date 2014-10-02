import webapp2

from google.appengine.ext.webapp.util import run_wsgi_app
from models.ndb import accounts

# Configs for the WSGI application.
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'something-very-very-secret',
}
config['webapp2_extras.auth'] = {
    'user_model': accounts.Account,
}

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', name='home',
                  handler='controllers.home.Home:index'),
    webapp2.Route(r'/signup', name='signup', methods=['GET'],
                  handler='controllers.accounts.Accounts:signup'),
    webapp2.Route(r'/signup', name='signup_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:signup_post'),
    webapp2.Route(r'/login', name='login_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:login_post'),
    webapp2.Route(r'/logout', name='logout',
                  handler='controllers.accounts.Accounts:logout'),
], debug=True, config=config)


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
