from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb


class BaseApiModel(EndpointsModel):
    """Base for all API models."""
    success_message = ndb.StringProperty()
    error_message = ndb.StringProperty()
