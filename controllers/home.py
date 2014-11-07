from controllers import base

from models.kinds.contacts import ContactUs


class Home(base.BaseHandler):

    def index(self):
        self.render('home/landing.html', {})

    def submit_contact(self):
        """Contact info POST request."""
        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        email = self.request.get('email')

        signee = ContactUs(first_name=first_name, last_name=last_name,
                           email=email)
        signee.put()

        return self.redirect_to('thank_you')

    def thankyou(self):
        self.render('home/thankyou.html', {})
