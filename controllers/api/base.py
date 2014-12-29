"""Common common that all API classes should import."""
import main
import services.exp as exp
from controllers import base

import endpoints
import endpoints.api_exceptions as api_exceptions
import os
import webapp2
from google.appengine.ext.endpoints import api_config


# Endpoints doesn't pass cookies by default on appspot.
AUTH_CONFIG = api_config.ApiAuth(allow_cookie_auth=True)


humanlink_api = endpoints.api(name='humanlink', version='v1',
                              description='HumanLink API', auth=AUTH_CONFIG)


def user_required(func):
    """Decorator that asserts the user is authorized."""
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


def handle_exception(e):
    """Raises an exception with appropriate HTTP status code."""
    maps = {
        exp.ServiceExp: api_exceptions.ServiceException,
        exp.PermissionExp: api_exceptions.ForbiddenException,
        exp.NotFoundExp: api_exceptions.NotFoundException,
        exp.ValueExp: api_exceptions.BadRequestException,
        exp.BadRequestExp: api_exceptions.BadRequestException,
    }
    raise maps[e.__class__](e.message)
