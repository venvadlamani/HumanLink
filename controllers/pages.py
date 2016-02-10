from controllers import base


class Pages(base.BaseHandler):
    """Simple pages that require no logic."""

    def terms(self):
        self.render('pages/terms.html', {})

    def privacy(self):
        self.render('pages/privacy.html', {})
