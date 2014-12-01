from controllers import base


class Invoice(base.BaseHandler):
    """Invoice related controller."""

    def index(self):
        """Index page."""
        self.render('invoice/index.html', {})
