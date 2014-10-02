import webapp2

from webapp2_extras import (
    auth,
    jinja2,
    sessions
)


# Default jinja2 configs.
jinja2.default_config['template_path'] = 'views'


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
            return self.redirect_to('signup')
        else:
            return func(self, *args, **kwargs)
    return check_login


class BaseHandler(webapp2.RequestHandler):
    """Base handler for all controllers."""

    @webapp2.cached_property
    def jinja2(self):
        """Returns a jinja2 renderer cached in the app registry.
        See jinja2.default_config for default jinja2 configs."""
        return jinja2.get_jinja2(app=self.app)

    def render(self, template, context):
        """Renders a template and writes the result to the response."""
        context['user'] = self.user_model
        rv = self.jinja2.render_template(template, **context)
        self.response.write(rv)

    @webapp2.cached_property
    def session_store(self):
        return sessions.get_store(request=self.request)

    @webapp2.cached_property
    def session(self):
        """Current session."""
        return self.session_store.get_session(backend="datastore")

    def dispatch(self):
        """Persist changes made to the session object."""
        try:
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
