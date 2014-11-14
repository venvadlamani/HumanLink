import json
import logging

from controllers import base
from controllers.base import login_required

from webapp2_extras import auth


class Accounts(base.BaseHandler):
    """Accounts and profiles related controller."""

    def index(self):
        """Index page."""
        self.render('accounts/index.html', {})

    def signup_post(self):
        """Sign-up POST request.

        TODO(kanat): Properly accept and return json objects.
        """
        body = json.loads(self.request.body)
        email = body['email']
        pass_raw = body['password']
        pass_raw_conf = body['password_confirm']
        logging.info('use me: %s' % pass_raw_conf)
        auth_id = 'local:' + email
        success, info = self.auth.store.user_model.create_user(
            auth_id=auth_id,
            unique_properties=['email'],
            email=email,
            password_raw=pass_raw)
        if success:
            logging.info('Signup success. email: %s' % email)
            return self.redirect_to('thank_you')
        else:
            logging.info('Signup failed. email: %s' % email)
            return self.redirect_to('signup')

    def login_post(self):
        """Log-in POST request.

        TODO(kanat): Properly accept and return json objects.
        """
        body = json.loads(self.request.body)
        email = body['email']
        pass_raw = body['password']
        auth_id = 'local:' + email
        try:
            self.auth.get_user_by_password(auth_id=auth_id,
                                           password=pass_raw,
                                           remember=True)
        except (auth.InvalidAuthIdError, auth.InvalidPasswordError) as e:
            logging.info('Invalid auth. email: %s' % email)
            raise e
        return self.redirect_to('home')

    @login_required
    def logout(self):
        """Log-out the current user.
        Redirects to home page after logging out."""
        self.auth.unset_session()
        return self.redirect_to('home')
