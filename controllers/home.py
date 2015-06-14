from controllers import base

from models.kinds.contacts import ContactUs


class Home(base.BaseHandler):

    def index(self):
        self.render('home/landing.html')

    def caregivers(self):
        self.render('home/caregivers.html')

    def POST_submit_contact(self):
        """Contact info POST request."""

        name = self.request_json.get('name', '(not provided)')
        email = self.request_json.get('email', '(not provided)')
        interest = int(self.request_json.get('interest', 0))
        zipcode = self.request_json.get('zipcode', '(not provided)')
        signee = ContactUs(name=name, email=email,
                           zipcode=zipcode, interest=interest)
        signee.put()

        self.write_json({'message': 'Thank you.'})