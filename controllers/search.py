from controllers import base


class Search(base.BaseHandler):
    """Caregiver search controller."""

    def index(self):
        """Index page."""
        self.render('search/index.html', {})
