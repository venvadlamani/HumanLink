from controllers import base


class Dashboard(base.BaseHandler):
    """Dashboard related controller."""

    def index(self):
        """Index page."""
        self.render('dashboard/index.html', {})
