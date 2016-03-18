import services.accounts
import services.email
import services.exp as exp
from controllers import base
from controllers.base import login_required
from models.kinds.structs import AccountType
from models.kinds.accounts import Account
from models.kinds.accounts import Caregiver
from models.kinds.accounts import Seeker
from models.kinds.connections import ConnList
from models.kinds.connections import ConnRequest
import logging
from webapp2_extras import auth
from webapp2_extras import security


class Accounts(base.BaseHandler):
    """Accounts and profiles related controller."""

    def index(self):
        """Index page."""
        self.render('accounts/index.html', {})

    def POST_signup(self):
        """Sign-up POST request."""
        email = self.request_json['email']
        pass_raw = self.request_json['password']

        account = services.accounts.create_account(email, pass_raw)

        if account:
            logging.info('Signup success. email: %s' % email)
            self.write_json({'status': 'success'})
        else:
            logging.info('Signup failed. email: %s' % email)
            raise exp.ServiceExp()

    def POST_login(self):
        """Log-in POST request.

        TODO(kanat): Handle errors properly.
        """
        email = self.request_json['email']
        pass_raw = self.request_json['password']
        auth_id = 'local:' + email.lower()
        try:
            self.auth.get_user_by_password(auth_id=auth_id,
                                           password=pass_raw,
                                           remember=True)
            self.write_json({'status': 'success'})
        except auth.InvalidAuthIdError:
            logging.info('Invalid email: %s' % email)
            raise exp.BadRequestExp('We do not recognize that email.')
        except auth.InvalidPasswordError:
            logging.info('Invalid password. email: %s' % email)
            raise exp.BadRequestExp('You entered a wrong password.')

    def POST_password_reset(self):
        """Send request to reset the password."""
        email = self.request_json['email']
        qry = Account.query(Account.email == email).fetch()
        account_id = ''
        for row in qry:
            account_id = row.key.id()

        services.email.send_password_reset(account_id)

    def POST_password_reset_form(self):
        """actually reset the password"""
        email = self.request.get('email', '')
        token = self.request.get('token', '')

        try:
            if not email or not token:
                raise exp.ServiceExp('Invalid email or verification token.')
            email = self.request_json.get('email')
            qry = Account.query(Account.email == email)
            for row in qry:
                acct = row.key.get()
                acct.password = security.generate_password_hash(
                    self.request_json.get('password'), length=12)
                acct.put()

            msg = '{} has been confirmed.'.format(email)
            alert = {'type': 'success', 'message': msg}
        except exp.ServiceExp as e:
            alert = {'type': 'danger', 'message': e.message}
        self.session.add_flash('alert', alert)
        return self.redirect('/accounts#/settings/profile')

    @login_required
    def logout(self):
        """Log-out the current user and redirect to home page."""
        self.auth.unset_session()
        return self.redirect_to('accounts_index')

    @login_required
    def userdata(self):
        """Retrieve minimal user-data about the current user from memcache.

        :return: a dictionary of small subset of account information.
        """
        self.write_json(self.user_data)

    def verify_email(self):
        """Verify an account's email."""
        email = self.request.get('email', '')
        token = self.request.get('token', '')
        try:
            if not email or not token:
                raise exp.ServiceExp('Invalid email or verification token.')
            account = services.accounts.verify_email(email, token)
            msg = '{} has been confirmed.'.format(account.email)
            alert = {'type': 'success', 'message': msg}
        except exp.ServiceExp as e:
            alert = {'type': 'danger', 'message': e.message}
        self.session.add_flash('alert', alert)
        return self.redirect('/accounts#/settings/profile')

    @login_required
    def POST_contact(self):
        """Send request to the Helpdesk and log it."""
        email = self.request_json['email']
        message = self.request_json['message']
        user_address = 'ven@humanlink.co'
        services.email.send_email_to_support(email, user_address, message)

    @login_required
    def GET_basic(self):
        """Basic account profile GET request."""
        basic_map = {}
        email = self.request.get('email')
        qry = Account.query(Account.email == email).fetch()

        for row in qry:
            basic_map = {
                'first': row.first,
                'last': row.last,
                'phone_number': row.phone_number,
                'email': row.email,
            }

        self.write_json(basic_map)

    @login_required
    def POST_basic(self):
        """Basic account profile POST request."""
        account_email = self.request_json.get('email')
        qry = Account.query(Account.email == account_email).fetch()

        for row in qry:
            new_basic = row.key.get()
            new_basic.first = self.request_json.get('first')
            new_basic.last = self.request_json.get('last')
            new_basic.phone_number = int(self.request_json.get('phone_number'))
            new_basic.put()

    @login_required
    def GET_caregiver_profile(self):
        """ Get the caregiver profile for the current account user

        params: account_id
        :return:caregiver profile map
        """
        caregiver_map = {}
        account_id = self.request.get('account_id')
        qry = Caregiver.query(Caregiver.account_id == int(account_id)).fetch()

        if len(qry) > 0:
            for row in qry:
                caregiver_map = {
                    'city': row.city,
                    'zipcode': row.zipcode,
                    'county': row.county,
                    'gender': row.gender,
                    'live_in': row.live_in,
                    'school': row.school,
                    'lpn': row.lpn,
                    'cna': row.cna,
                    'hcs': row.hcs,
                    'iha': row.iha,
                    'ad': row.ad,
                    'headline': row.headline,
                    'bio': row.bio,
                    'weekdays': row.weekdays,
                    'weekends': row.weekends,
                    'cats': row.cats,
                    'dogs': row.dogs,
                    'smoking': row.smoking,
                }
            self.write_json(caregiver_map)
        else:
            self.write_json(
                {
                    'count': '0',
                    'message': 'Care provider profile doesnt exist. Please create one.'
                })

    @login_required
    def POST_caregiver_profile(self):
        """ Update the caregiver profile for the current account user

        params: caregiver profile data
        :return:success/error message
        """
        account_id = self.request_json.get('account_id')
        qry = Caregiver.query(Caregiver.account_id == int(account_id)).fetch()

        if len(qry) > 0:
            for row in qry:
                row.city = self.request_json.get('city')
                row.zipcode = self.request_json.get('zipcode')
                row.county = self.request_json.get('county')
                row.gender = self.request_json.get('gender')
                row.live_in = self.request_json.get('live_in')
                row.school = self.request_json.get('school')
                row.lpn = self.request_json.get('lpn')
                row.cna = self.request_json.get('cna')
                row.hcs = self.request_json.get('hcs')
                row.iha = self.request_json.get('iha')
                row.ad = self.request_json.get('ad')
                row.headline = self.request_json.get('headline')
                row.bio = self.request_json.get('bio')
                row.weekdays = self.request_json.get('weekdays')
                row.weekends = self.request_json.get('weekends')
                row.cats = self.request_json.get('cats')
                row.dogs = self.request_json.get('dogs')
                row.smoking = self.request_json.get('smoking')
                row.put()
            self.write_json({'message': 'Caregiver profile has been updated.'})
        else:
            cgvr = Caregiver()
            cgvr.account_id = int(account_id)
            cgvr.city = self.request_json.get('city')
            cgvr.zipcode = self.request_json.get('zipcode')
            cgvr.county = self.request_json.get('county')
            cgvr.gender = self.request_json.get('gender')
            cgvr.live_in = self.request_json.get('live_in')
            cgvr.school = self.request_json.get('school')
            cgvr.lpn = self.request_json.get('lpn')
            cgvr.cna = self.request_json.get('cna')
            cgvr.hcs = self.request_json.get('hcs')
            cgvr.iha = self.request_json.get('iha')
            cgvr.ad = self.request_json.get('ad')
            cgvr.headline = self.request_json.get('headline')
            cgvr.bio = self.request_json.get('bio')
            cgvr.weekdays = self.request_json.get('weekdays')
            cgvr.weekends = self.request_json.get('weekends')
            cgvr.cats = self.request_json.get('cats')
            cgvr.dogs = self.request_json.get('dogs')
            cgvr.smoking = self.request_json.get('smoking')
            cgvr.put()
            self.write_json({'message': 'Caregiver profile has been created.'})

    @login_required
    def POST_seeker_profile(self):
        """ Update the seeker profile

        params: seeker profile data
        :return: success/error message
        """
        account_id = self.request_json.get('account_id')
        qry = Seeker.query(Seeker.account_id == int(account_id)).fetch()

        if len(qry) > 0:
            for row in qry:
                row.team_name = self.request_json.get('team_name')
                row.mission = self.request_json.get('mission')
                row.main_phone = self.request_json.get('main_phone')
                row.website = self.request_json.get('website')
                row.video = self.request_json.get('video')
                row.email = self.request_json.get('email')
                row.caregiver_needs = self.request_json.get('caregiver_needs')
                row.hoyer_lift = self.request_json.get('hoyer_lift')
                row.cough_assist = self.request_json.get('cough_assist')
                row.adaptive_utensil = self.request_json.get('adaptive_utensil')
                row.meal_prep = self.request_json.get('meal_prep')
                row.housekeeping = self.request_json.get('housekeeping')
                row.put()

            self.write_json({'message': 'Caregiver profile has been updated.'})
        else:
            skr = Seeker()
            skr.account_id = int(account_id)
            skr.team_name = self.request_json.get('team_name')
            skr.mission = self.request_json.get('mission')
            skr.main_phone = self.request_json.get('main_phone')
            skr.website = self.request_json.get('website')
            skr.video = self.request_json.get('video')
            skr.email = self.request_json.get('email')
            skr.caregiver_needs = self.request_json.get('caregiver_needs')
            skr.hoyer_lift = bool(self.request_json.get('hoyer_lift'))
            skr.cough_assist = self.request_json.get('cough_assist')
            skr.adaptive_utensil = self.request_json.get('adaptive_utensil')
            skr.meal_prep = self.request_json.get('meal_prep')
            skr.housekeeping = self.request_json.get('housekeeping')
            skr.put()

    @login_required
    def GET_connections(self):
        """ Get the current accounts connections

        params: account_id
        :return: return connections
        """
        account_id = int(self.request.get('account_id'))
        qry = ConnRequest.query(ConnList.account_id == account_id).fetch()

        if len(qry) > 0:
            print "==="
            print qry
        else:
            self.write_json(
                {
                    'count': '0',
                    'message': 'You have no connections.'
                })
