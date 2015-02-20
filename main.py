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

    webapp2.Route(r'/login.json', name='login_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:login_post'),

    webapp2.Route(r'/logout', name='logout', methods=['GET'],
                  handler='controllers.accounts.Accounts:logout'),

    webapp2.Route(r'/signup.json', name='signup_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:signup_post'),

    webapp2.Route(r'/accounts/userdata.json', name='userdata', methods=['GET'],
                  handler='controllers.accounts.Accounts:userdata'),

    webapp2.Route(r'/submit_contact', name='submit_contact', methods=['POST'],
                  handler='controllers.home.Home:submit_contact'),

    webapp2.Route(r'/terms', name='terms', methods=['GET'],
                  handler='controllers.pages.Pages:terms'),

    webapp2.Route(r'/connections', name='connections', methods=['GET'],
                  handler='controllers.connections.Connections:index'),

    webapp2.Route(r'/favorites', name='favorites', methods=['GET'],
                  handler='controllers.favorites.Favorites:index'),

    webapp2.Route(r'/invoice', name='invoice', methods=['GET'],
                  handler='controllers.invoice.Invoice:index'),

    webapp2.Route(r'/jobs', name='jobs', methods=['GET'],
                  handler='controllers.jobs.Jobs:index'),

    webapp2.Route(r'/messages', name='messages', methods=['GET'],
                  handler='controllers.messages.Messages:index'),

    webapp2.Route(r'/dashboard', name='dashboard', methods=['GET'],
                  handler='controllers.dashboard.Dashboard:index'),

], debug=True, config=config)
