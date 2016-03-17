from google.appengine.api import taskqueue
from google.appengine.ext import ndb
from controllers import base
from models.kinds.structs import AccountType
from models.kinds.home import ContactUs
from models.kinds.accounts import Caregiver
from models.kinds.accounts import Seeker
from models.kinds.accounts import Account
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
        @return: returns a dictionary of caregiver
        """
        caregiver_map = {}
        account_id = int(self.request.get('account_id'))
        qry = Caregiver.query(Caregiver.account_id == account_id).fetch()

        for caregiver in qry:
            cgvr_account = Account.query(
                Account.caregiver_id == caregiver.key.id()).fetch()
            caregiver_map = {
                'first_name': cgvr_account[0].first,
                'last_name': cgvr_account[0].last,
                'phone_number': cgvr_account[0].phone_number,
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
                'phone_verified': caregiver.phone_verified,
                'background_verified': caregiver.background_verified,
                'offlineID_verified': caregiver.offlineID_verified,
            }
        self.write_json(caregiver_map)

    #   PROVIDER SEARCH
    def GET_caregivers(self):
        """Caregiver General GET request.

        @return: returns a dictionary of all caregivers registered as guests in the system
        """
        search_string = self.request.get('search_string')
        caregiver_array = []

        #   currently expecting Geo based searches. In the future Search needs will change
        if search_string:
            caregiver_query = Caregiver.query(ndb.OR(Caregiver.city == search_string,
                                                     Caregiver.zipcode == search_string,
                                                     Caregiver.county == search_string)).fetch()
        else:
            caregiver_query = Caregiver.query().fetch()

        if len(caregiver_query) > 0:
            for row in caregiver_query:
                if (
                                row.offlineID_verified and row.background_verified and row.phone_verified):
                    cgvr_account = Account.get_by_id(row.account_id)
                    caregiverMap = {
                        'first_name': cgvr_account.first,
                        'last_name': cgvr_account.last,
                        'phone_number': cgvr_account.phone_number,
                        'account_id': row.account_id,
                        'headline': row.headline,
                        'bio': row.bio,
                        'city': row.city,
                        'offlineID_verified': row.offlineID_verified,
                        'phone_verified': row.phone_verified,
                        'background_verified': row.background_verified,
                    }
                    caregiver_array.append(caregiverMap)
            self.write_json(caregiver_array)
        else:
            self.write_json(
                {
                    'count': '0',
                    'message': 'No care providers exist.'
                })

    # SEEKER SEARCH
    def GET_seekers(self):
        """ Search for care seekers request.

        @return: returns a dictionary of all caregivers registered as guests in the system
        """
        seeker_array = []

        #   currently expecting Geo based searches. In the future Search needs will change
        seeker_query = Seeker.query().fetch()

        if len(seeker_query) > 0:
            for row in seeker_query:
                seekerMap = {
                    'account_id': row.account_id,
                    'team_name': row.team_name,
                    'mission': row.mission,
                    'main_phone': row.main_phone,
                    'website': row.website,
                }
                seeker_array.append(seekerMap)
            self.write_json(seeker_array)
        else:
            self.write_json(
                {
                    'count': '0',
                    'message': 'No care seekers exist.'
                })

    def GET_seeker_profile(self):
        """GET seeker profile.

        @params: account_id
        @return: returns seeker profile
        """
        seeker_map = {}
        account_id = int(self.request.get('account_id'))
        qry = Seeker.query(Seeker.account_id == account_id).fetch()
        for row in qry:
            seeker_map = {
                'team_name': row.team_name,
                'mission': row.mission,
                'main_phone': row.main_phone,
                'website': row.website,
                'video': row.video,
                'email': row.email,
                'caregiver_needs': row.caregiver_needs,
                'hoyer_lift': row.hoyer_lift,
                'cough_assist': row.cough_assist,
                'adaptive_utensil': row.adaptive_utensil,
                'meal_prep': row.meal_prep,
                'housekeeping': row.housekeeping,
            }

        self.write_json(seeker_map)
