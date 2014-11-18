from controllers import base


class Messages(base.BaseHandler):
    """Messages related controller."""

    def index(self):
        """Index page."""
        self.render('messages/index.html', {})
