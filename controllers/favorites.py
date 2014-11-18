from controllers import base


class Favorites(base.BaseHandler):
    """Favorites related controller."""

    def index(self):
        """Index page."""
        self.render('favorites/index.html', {})
