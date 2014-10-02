from google.appengine.ext import ndb


class Base(ndb.Model):
    """Base NDB model."""

    created = ndb.DateTimeProperty(auto_now_add=True)
    modified = ndb.DateTimeProperty(auto_now=True)
