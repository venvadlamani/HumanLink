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


def get_current_user():
    """Returns the user who is currently logged in on the website."""
    handler = FakeRequest()
    return handler.get_current_user()


def refresh_userdata():
    """Refreshes userdata that is in the memcache."""
    handler = FakeRequest()
    return handler.refresh_userdata()


class FakeRequest(object):
    """Simulates a webapp2 request.

    Since authentication is handled using cookies on the webapp2 side,
    this class simulates a webapp2 request.
    """

    @property
    def handler(self):
        if not getattr(self, '_handler', None):
            req = webapp2.Request(dict(os.environ))
            req.app = webapp2.WSGIApplication(config=main.config)
            self._handler = base.BaseHandler(request=req)
        return self._handler

    def get_current_user(self):
        return self.handler.user_model

    def refresh_userdata(self):
        self.handler._store_userdata()
