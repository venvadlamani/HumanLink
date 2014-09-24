import jinja2
import webapp2

from webapp2_extras import jinja2


# Default jinja2 configs.
jinja2.default_config['template_path'] = 'views'


class BaseHandler(webapp2.RequestHandler):
    """Base handler for all controllers."""

    @webapp2.cached_property
    def jinja2(self):
        """Returns a jinja2 renderer cached in the app registry.
        See jinja2.default_config for default jinja2 configs."""
        return jinja2.get_jinja2(app=self.app)

    def render(self, template, **context):
        """Renders a template and writes the result to the response."""
        rv = self.jinja2.render_template(template, **context)
        self.response.write(rv)
