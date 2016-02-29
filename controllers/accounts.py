import services.accounts
import services.email
import services.exp as exp
from controllers import base
from controllers.base import login_required
from models.kinds.structs import AccountType
from models.kinds.accounts import Account
from models.kinds.accounts import Caregiver
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
        pass_raw_conf = self.request_json['password_confirm']
        account_type = int(self.request_json['account_type'])

        if pass_raw != pass_raw_conf:
            raise exp.ValueExp('Password does not match confirmation.')
        if not 0 <= account_type <= 2:
            raise exp.ValueExp('Invalid account type.')

        account = services.accounts.create_account(
            email, pass_raw, AccountType(account_type))
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
        qry = Account.query(Account.email == account_email)

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

    @login_required
    def POST_caregiver_profile(self):
        """ Update the caregiver profile for the current account user
        params: caregiver profile data
        :return:caregiver profile map
        """
        account_id = self.request_json.get('account_id')
        qry = Caregiver.query(Caregiver.account_id == int(account_id)).fetch()
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

    @login_required
    def GET_caregiver_profile_preview(self):
        """ Get the caregiver profile preview for the current account user
        params: account_id
        :return:caregiver profile map
        """
        caregiver_map = {}
        account_map = {}
        account_id = self.request.get('account_id')
        email = self.request.get('email')

        qry_cgr = Caregiver.query(Caregiver.account_id == int(account_id)).fetch()
        for row in qry_cgr:
            caregiver_map = {
                'city': row.city,
                'county': row.county,
                'zipcode': row.zipcode,
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

        qry_acct = Account.query(Account.email == email).fetch()
        for row in qry_acct:
            account_map = {
                'first_name': row.first,
                'last_name': row.last,
                'phone_number': row.phone_number,
                'phone_number_verified ': row.phone_number_verified,
                'email_verified': row.email_verified,
                'background_verified': row.background_verified,
            }

        profile_map = {
            'caregiver': caregiver_map,
            'account': account_map
        }
        self.write_json(profile_map)
