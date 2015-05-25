import common
import configs
import routes
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

application = webapp2.WSGIApplication(
    routes.routes, debug=not common.is_prod(), config=config)
