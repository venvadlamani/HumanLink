from controllers import base


class Jobs(base.BaseHandler):
    """Jobs related controller."""

    def index(self):
        """Index page."""
        self.render('jobs/index.html', {})
