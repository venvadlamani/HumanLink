import services.accounts

import json
import logging
import webapp2
from google.appengine.api import memcache
from webapp2_extras import (
    auth,
    jinja2,
    sessions
)


# Default jinja2 configs.
jinja2.default_config['template_path'] = 'views'
env_args = {
    'block_start_string': '[%',
    'block_end_string': '%]',
    'variable_start_string': '[=',
    'variable_end_string': '=]',
}
jinja2.default_config['environment_args'].update(env_args)
jinja2.default_config['filters'] = {
    'tojson': lambda obj: json.dumps(_json_encode(obj)),
}


def login_required(func):
    """Decorator that requires the user to be logged in
    to use a given method.
    Redirects to the login page if not logged in.

    Usage:
        @login_required
        def profile(self):
            ...
    """
    def check_login(self, *args, **kwargs):
        if not self.user:
            if self._is_json_request():
                self.abort(401, detail='Authorization required.')
            else:
                return self.redirect_to('accounts_index')
        else:
            return func(self, *args, **kwargs)
    return check_login


class BaseHandler(webapp2.RequestHandler):
    """Base handler for all controllers."""

    # This property will be populated if the request is /json.
    request_json = None

    @webapp2.cached_property
    def jinja2(self):
        """Returns a jinja2 renderer cached in the app registry.
        See jinja2.default_config for default jinja2 configs."""
        return jinja2.get_jinja2(app=self.app)

    def render(self, template, context={}):
        """Renders a template and writes the result to the response."""
        context['userdata'] = self.user_data
        rv = self.jinja2.render_template(template, **context)
        self.response.write(rv)

    def write_json(self, response):
        """Writes a JSON response.

        This should be used with a JSON API method."""
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(_json_encode(response)))

    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

    @webapp2.cached_property
    def session(self):
        """Current session."""
        return self.session_store.get_session(backend="datastore")

    def dispatch(self):
        """Dispatch an incoming request.
        This method also persists session object after the request.
        """
        try:
            # Handle JSON requests slightly differently.
            if self._is_json_request():
                self.request_json = (self.request.GET
                                     if self.request.method == 'GET' else
                                     json.loads(self.request.body))
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def auth(self):
        """Handles user authentication."""
        return auth.get_auth(request=self.request)

    @webapp2.cached_property
    def user(self):
        """This just returns a minimal info about the user."""
        user = self.auth.get_user_by_session()
        return user

    @webapp2.cached_property
    def user_model(self):
        """Gets the user object for the user from the datastore."""
        user_model, timestamp = self.auth.store.user_model.get_by_auth_token(
            self.user['user_id'],
            self.user['token']) if self.user else (None, None)
        return user_model

    @webapp2.cached_property
    def user_data(self):
        """Retrieves user-data from memcache if available.

        If not in memcache, retrieve the data from datastore and store in
        memcache.

        :param account_id: ID of the account.
        :return: (dict)
        """
        if not self.user:
            return
        account_id = self.user['user_id']
        userdata = memcache.get('userdata:{}'.format(account_id))
        if userdata:
            logging.info('Memcache hit.')
            return userdata
        logging.info('Memcache miss.')
        return self._store_userdata()

    def _store_userdata(self, time=3600):
        """Stores user-data in memcache.

        This method should be called manually if account information is updated.
        """
        if not self.user:
            return
        account_id = self.user['user_id']
        account = services.accounts.account_by_id(account_id)
        userdata = {
            'account_id': account.id,
            'account_type': account.account_type.name,
            'first': account.first,
            'last': account.last,
            'name': (account.first or '') + ' ' + (account.last or ''),
            'email': account.email,
            'email_verified': account.email_verified,
            'picture_url': '',
        }
        memcache.set('userdata:{}'.format(account_id), userdata, time=time)
        return userdata

    def handle_exception(self, exception, debug):
        """Exception handler for a webapp2 request.

        TODO(kanat): Implement this similar to api.base.handle_exception.
        """
        logging.exception(exception)
        result = {
            'status': 'error',
            'status_code': getattr(exception, 'code', 400),
            'error_message': getattr(exception, 'message', 'Unexpected error.'),
        }
        self.response.headers.add_header('Content-Type', 'application/json')
        self.response.write(json.dumps(_json_encode(result)))
        self.response.set_status(result['status_code'])

    def _is_json_request(self):
        return (self.request.path.endswith('.json')
                or self.request.content_type == 'application/json')


def _json_encode(obj):
    """Custom JSON encoder for types that aren't handled by default."""
    from datetime import datetime
    from protorpc import messages
    from google.appengine.ext import ndb

    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, messages.Enum):
        return obj.name
    if isinstance(obj, (int, long)) and obj >= (1 << 31):
        return str(obj)
    if isinstance(obj, ndb.Key):
        return str(obj.id())
    if isinstance(obj, dict):
        return {k: _json_encode(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return map(_json_encode, obj)
    return obj
