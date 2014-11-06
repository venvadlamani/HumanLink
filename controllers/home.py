from controllers import base

from models.kinds.contacts import ContactUs


class Home(base.BaseHandler):

    def index(self):
        self.render('home/landing.html', {})

    def submit_contact(self):
        """Contact info POST request."""
        first_name = self.request.get('fname')
        last_name = self.request.get('lname')
        email = self.request.get('email')
        phone = self.request.get('phone')
        comment = self.request.get('comment')

        signee = ContactUs(firstname=first_name, lastname=last_name,
                           phone_number=phone, email=email, comment=comment)
        signee.put()

        return self.redirect_to('thank_you')

    def thankyou(self):
        self.render('home/thankyou.html', {})
