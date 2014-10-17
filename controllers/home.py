from controllers import base

from models.kinds.contacts import ContactUs


class Home(base.BaseHandler):

    def index(self):
        self.render('home/index.html', {})

    def submit_contact(self):
        """Contact info POST request."""
        name = self.request.get('name')
        email = self.request.get('email')
        phone = self.request.get('phone')
        comment = self.request.get('comment')

        signee = ContactUs(name=name, phone_number=phone,
                           email=email, comment=comment)
        signee.put()

        return self.redirect_to('thank_you')

    def thankyou(self):
        self.render('home/thankyou.html', {})
