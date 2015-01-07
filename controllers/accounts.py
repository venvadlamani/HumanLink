import services.accounts
import services.exp as exp
from controllers import base
from controllers.base import login_required
from models.kinds.structs import AccountType

import logging
from google.appengine.api import memcache
from webapp2_extras import auth


class Accounts(base.BaseHandler):
    """Accounts and profiles related controller."""

    def index(self):
        """Index page."""
        self.render('accounts/index.html', {})

    def signup_post(self):
        """Sign-up POST request.

        TODO(kanat): Handle errors properly.
        """
        email = self.request_json['email']
        pass_raw = self.request_json['password']
        pass_raw_conf = self.request_json['password_confirm']
        logging.info('use me: %s' % pass_raw_conf)
        account = services.accounts.create_account(
            email, pass_raw, AccountType.Caregiver)
        if account:
            logging.info('Signup success. email: %s' % email)
            self.write_json({'status': 'success'})
        else:
            logging.info('Signup failed. email: %s' % email)
            raise exp.ServiceExp()

    def login_post(self):
        """Log-in POST request.

        TODO(kanat): Handle errors properly.
        """
        email = self.request_json['email']
        pass_raw = self.request_json['password']
        auth_id = 'local:' + email
        try:
            self.auth.get_user_by_password(auth_id=auth_id,
                                           password=pass_raw,
                                           remember=True)
            self.write_json({'status': 'success'})
        except (auth.InvalidAuthIdError, auth.InvalidPasswordError) as e:
            logging.info('Invalid auth. email: %s' % email)
            raise exp.BadRequestExp()

    @login_required
    def logout(self):
        """Log-out the current user and redirect to home page."""
        self.auth.unset_session()
        return self.redirect_to('home')

    @login_required
    def userdata(self):
        """Retrieve minimal user-data about the current user from memcache.

        :return: a dictionary of small subset of account information.
        """
        userdata = self._retrieve_userdata(self.user['user_id'])
        self.write_json(userdata)

    def _store_userdata(self, account_id, time=3600):
        """Stores user-data in memcache.

        This method should be called manually if account information is updated.

        :param account_id: ID of the account.
        :return: see self.userdata() return value.
        """
        account = services.accounts.account_by_id(account_id)
        userdata = {
            'account_id': account.id,
            'account_type': account.account_type.name,
            'first': account.first,
            'last': account.last,
            'email': account.email,
            'email_verified': account.email_verified,
            'picture_url': '',
        }
        memcache.set('userdata:{}'.format(account_id), userdata, time=time)
        return userdata

    def _retrieve_userdata(self, account_id):
        """Retrieves user-data from memcache if available.

        If not in memcache, retrieve the data from datastore and store in
        memcache.

        :param account_id: ID of the account.
        :return: see self.userdata() return value.
        """
        userdata = memcache.get('userdata:{}'.format(account_id))
        if userdata:
            logging.info('Memcache hit.')
            return userdata
        logging.info('Memcache miss.')
        return self._store_userdata(account_id)
