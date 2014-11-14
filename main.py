import configs
import webapp2

from models.kinds import accounts

# Configs for the WSGI application.
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': configs.SESSION_SECRET,
}
config['webapp2_extras.auth'] = {
    'user_model': accounts.Account,
    'session_backend': 'datastore',
}

application = webapp2.WSGIApplication([
    webapp2.Route(r'/', name='home', methods=['GET'],
                  handler='controllers.home.Home:index'),

    webapp2.Route(r'/accounts', name='accounts_index', methods=['GET'],
                  handler='controllers.accounts.Accounts:index'),

    webapp2.Route(r'/signup', name='signup_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:signup_post'),

    webapp2.Route(r'/login', name='login_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:login_post'),

    webapp2.Route(r'/logout', name='logout',
                  handler='controllers.accounts.Accounts:logout'),

    webapp2.Route(r'/submit_contact', name='submit_contact', methods=['POST'],
                  handler='controllers.home.Home:submit_contact'),

    webapp2.Route(r'/thankyou', name='thank_you', methods=['GET'],
                  handler='controllers.home.Home:thankyou'),

    webapp2.Route(r'/terms', name='terms', methods=['GET'],
                  handler='controllers.pages.Pages:terms'),

], debug=True, config=config)
