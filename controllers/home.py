import base


class Home(base.BaseHandler):

    def index(self):
        self.render('home/index.html', {})
