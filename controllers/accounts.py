import base
import logging

from base import login_required
from webapp2_extras import auth


class Accounts(base.BaseHandler):
    """Accounts and profiles related controller."""

    def signup(self):
        """Log-in or sign-up page."""
        self.render('accounts/signup.html', {})

    def signup_post(self):
        """Sign-up POST request."""
        name = self.request.get('name')
        email = self.request.get('email')
        pass_raw = self.request.get('password')
        pass_raw_conf = self.request.get('password_confirm')
        logging.info('use me: %s' % pass_raw_conf)
        auth_id = 'local:' + email
        success, info = self.auth.store.user_model.create_user(
            auth_id=auth_id,
            unique_properties=['email'],
            email=email,
            password_raw=pass_raw,
            name=name)
        if success:
            logging.info('Signup success. email: %s' % email)
            self.auth.get_user_by_password(auth_id=auth_id,
                                           password=pass_raw,
                                           remember=True)
            return self.redirect_to('home')
        else:
            logging.info('Signup failed. email: %s' % email)
            return self.redirect_to('signup')

    def login_post(self):
        """Log-in POST request."""
        email = self.request.get('email')
        pass_raw = self.request.get('password')
        auth_id = 'local:' + email
        try:
            self.auth.get_user_by_password(auth_id=auth_id,
                                           password=pass_raw,
                                           remember=True)
            return self.redirect_to('home')
        except (auth.InvalidAuthIdError, auth.InvalidPasswordError):
            logging.info('Invalid auth. email: %s' % email)
        logging.info('Some other authentication error.')
        return self.redirect_to('signup')

    @login_required
    def logout(self):
        """Log-out the current user.
        Redirects to home page after logging out."""
        self.auth.unset_session()
        self.redirect_to('home')
