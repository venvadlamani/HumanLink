from controllers import base


class Connections(base.BaseHandler):
    """Connections related controller."""

    def index(self):
        """Index page."""
        self.render('connections/index.html', {})
