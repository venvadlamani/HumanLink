from google.appengine.api import taskqueue
from controllers import base
from models.kinds.structs import AccountType
from models.kinds.home import ContactUs
from models.kinds.home import CaregiverGeneral
import logging
from models.kinds.home import Request


class Home(base.BaseHandler):
    def index(self):
        self.render('home/index.html')

    def POST_submit_contact(self):
        """Contact info POST request."""

        name = self.request_json.get('name', '(not provided)')
        email = self.request_json.get('email', '(not provided)')
        interest = int(self.request_json.get('interest', 0))
        zipcode = self.request_json.get('zipcode', '(not provided)')
        referrer = self.request_json.get('referrer', '')

        signee = ContactUs(name=name, email=email, zipcode=zipcode,
                           interest=interest, referrer=referrer)
        signee.put()

        taskqueue.add(url='/queue/slack', params={
            'text': 'New intererst! *{}* ({}) from *{}*.'
                      .format(name, AccountType(interest - 1), zipcode)
        })

        self.write_json({'message': 'Thank you.'})

    def POST_caregiver_general(self):
        """Caregiver General POST request."""

        caregiver = CaregiverGeneral()
        caregiver.name = self.request_json.get('name')
        caregiver.location = self.request_json.get('location')
        caregiver.phone_number = self.request_json.get('phone')
        caregiver.gender = self.request_json.get('gender')
        caregiver.live_in = self.request_json.get('live_in')
        caregiver.school = self.request_json.get('school')
        caregiver.lpn = self.request_json.get('lpn')
        caregiver.cna = self.request_json.get('cna')
        caregiver.hcs = self.request_json.get('hcs')
        caregiver.iha = self.request_json.get('iha')
        caregiver.ad = self.request_json.get('ad')
        caregiver.headline = self.request_json.get('headline')
        caregiver.bio = self.request_json.get('bio')
        caregiver.weekdays = self.request_json.get('weekdays')
        caregiver.weekends = self.request_json.get('weekends')

        caregiver.put()

        self.write_json({'message': 'Thank you.'})

    def GET_caregiver_general(self):
        """Caregiver General GET request.

        @return: returns a dictionary of all caregivers registered as guests in the system
        """

        caregiver_dict = {}
        caregiver_query = CaregiverGeneral.query().fetch()

        for caregiver in caregiver_query:
            if not caregiver.id in caregiver_dict:
                caregiverMap = {
                    'id': str(caregiver.id),
                    'name': caregiver.name,
                    'location': caregiver.location,
                    'photo': ('/images/' + caregiver.phone_number + '.png'),
                    'phone_number': caregiver.phone_number
                }
                logging.info(caregiverMap)
                caregiver_dict[caregiver.id] = caregiverMap

        self.write_json(caregiver_dict)

    def POST_submit_request(self):
        """Request info POST request."""

        name = self.request_json.get('name', '(not provided)')
        email = self.request_json.get('email', '(not provided)')
        message = self.request_json.get('message', '(not provided)')

        signee = Request(name=name, email=email, message=message)
        signee.put()

    def POST_contact_request(self):
        """General questions from users/guests POST request."""

        req = Request()
        req.name = self.request_json.get('name')
        req.email = self.request_json.get('email')
        req.message = self.request_json.get('message')

        req.put()

        self.write_json({'message': 'Thank you.'})
