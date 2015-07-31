from controllers import base


class Settings(base.BaseHandler):
    """Settings related controller."""

    def index(self):
        """Index page."""
        self.render('settings/index.html')