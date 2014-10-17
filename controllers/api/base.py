"""Common common that all API classes should import."""

import main

import endpoints
import os
import webapp2

from controllers import base


humanlink_api = endpoints.api(name='humanlink', version='v1',
                              description='HumanLink API')


def user_required(func):
    def check_login(self, *args, **kwargs):
        if not get_current_user():
            raise endpoints.UnauthorizedException('Invalid token.')
        else:
            return func(self, *args, **kwargs)
    return check_login


def get_current_user():
    """Returns the user who is currently logged in on the website.

    Since GAE allows authentication with Google Accounts only, this is a
    very hacky way to check if a user is authenticated on the website.
    """
    req = webapp2.Request(dict(os.environ))
    req.app = webapp2.WSGIApplication(config=main.config)

    fake_handler = base.BaseHandler(request=req)
    return fake_handler.user_model
