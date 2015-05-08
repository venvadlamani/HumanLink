"""Helper methods for different parts of the project."""

import os


def is_prod():
    """Returns whether or not running in production."""
    host = os.environ.get('HTTP_HOST', '')
    return (host.endswith('humanlink.co') or
            host.endswith('care-tiger.appspot.com'))


def is_staging():
    """Returns whether or not running in staging."""
    host = os.environ.get('HTTP_HOST', '')
    return not is_prod() and host.endswith('appspot.com')


def is_localhost():
    """Returns whether or not running in dev_appserver."""
    return os.environ.get('SERVER_SOFTWARE', '').startswith('Development')
