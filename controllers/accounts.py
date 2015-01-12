import services.accounts
import services.exp as exp
from controllers import base
from controllers.base import login_required
from models.kinds.structs import AccountType

import logging
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
        self.write_json(self.user_data)
