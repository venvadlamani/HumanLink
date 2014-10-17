from google.appengine.ext import ndb


class Base(ndb.Model):
    """Base NDB model."""

    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @property
    def id(self):
        if self.key:
            # For some weird reason, key.id() is sometimes type of `long.
            return int(self.key.id())
