from google.appengine.api import taskqueue
from controllers import base
from models.kinds.structs import AccountType
from models.kinds.home import ContactUs
from models.kinds.accounts import Caregiver
import services.email
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

        caregiver = Caregiver()
        caregiver.first_name = self.request_json.get('first_name')
        caregiver.last_name = self.request_json.get('last_name')
        caregiver.city = self.request_json.get('city')
        caregiver.county = self.request_json.get('county')
        caregiver.zipcode = self.request_json.get('zipcode')
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
        caregiver.cats = self.request_json.get('cats')
        caregiver.dogs = self.request_json.get('dogs')
        caregiver.smoking = self.request_json.get('smoking')

        caregiver.put()

        self.write_json({'message': 'Thank you.'})

    def GET_search_caregivers(self):
        """Caregiver General GET request.

        @return: returns a dictionary of all caregivers registered as guests in the system
        """
        search_string = ''
        caregiver_dict = Home.search_map(search_string)
        self.write_json(caregiver_dict)

    def POST_contact_request(self):
        """General questions from users/guests POST request."""
        req = Request()
        req.name = self.request_json.get('name')
        req.email = self.request_json.get('email')
        req.message = self.request_json.get('message')
        req.put()

        services.email.send_email_to_support(req.email, req.name, req.message)
        self.write_json({'message': 'Thank you.'})

    def GET_caregiver_profile(self):
        """Caregiver profile GET request.
        @params: Caregiver ID to be used for the search

        @return: returns a dictionary of caregiver registered as a guest in the system
        """
        caregiver_map = {}

        qry = Caregiver.query().fetch()

        for caregiver in qry:
            caregiver_map = {
                'name': caregiver.name,
                'phone_number_primary': caregiver.phone_number_primary,
                'phone_number_secondary': caregiver.phone_number_secondary,
                'county': caregiver.county,
                'city': caregiver.city,
                'zipcode': caregiver.zipcode,
                'gender': caregiver.gender,
                'live_in': caregiver.live_in,
                'school': caregiver.school,
                'lpn': caregiver.lpn,
                'cna': caregiver.cna,
                'iha': caregiver.iha,
                'ad': caregiver.ad,
                'hcs': caregiver.hcs,
                'headline': caregiver.headline,
                'bio': caregiver.bio,
                'weekends': caregiver.weekends,
                'weekdays': caregiver.weekdays,
                'cats': caregiver.cats,
                'dogs': caregiver.dogs,
                'smoking': caregiver.smoking,
            }
        self.write_json(caregiver_map)

    def GET_search_refined(self):
        """Refined Caregiver search request.
        @params: Location where caregivers are needed

        @return: returns a dictionary of caregiver registered as a guests (FOR NOW)
        in the system registered for a certain location
        """
        search_string = self.request_json.get('search')
        caregiver_dict = Home.search_map(search_string)
        self.write_json(caregiver_dict)

    @staticmethod
    def search_map(search_string):
        caregiver_dict = {}
        print '-------------------'
        print search_string

        if search_string:
            caregiver_query = Caregiver.query(Caregiver.city ==
                                              search_string).fetch()
        else:
            caregiver_query = Caregiver.query().fetch()

        for caregiver in caregiver_query:
            if not caregiver.id in caregiver_dict:
                caregiverMap = {
                    'id': caregiver.key,
                    'city': caregiver.city,
                }
                caregiver_dict[caregiver.id] = caregiverMap

        return caregiver_dict
