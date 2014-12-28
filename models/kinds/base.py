from google.appengine.ext import ndb


class Base(ndb.Model):
    """Base NDB model.

    All NDB models that are persisted in the datastore should inherit from this.
    """
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @property
    def id(self):
        if isinstance(self.key, ndb.Key):
            return self.key.id()

    @classmethod
    def get_key(cls, cls_id=None):
        """Returns self.key() if exists or builds a key using cls_id provided.

        :param cls_id: (int) ID of the entity to build a key for.
        :return: (ndb.Key)
        """
        key = (cls.key if isinstance(cls.key, ndb.Key)
               else ndb.Key(cls._get_kind(), cls_id))
        return key

    @classmethod
    def ids_to_keys(cls, cls_ids):
        """Returns a list of ndb.Key`s from given IDs.

        :param cls_ids: (list<int>) List of entity IDs to build keys for.
        :return: (list<ndb.Key>)
        """
        return [cls.get_key(cls_id) for cls_id in cls_ids]
