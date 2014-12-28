from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb


class BaseApiModel(EndpointsModel):
    """Base API model."""
    # Included fields. If not provided, everything will be included.
    fields = ndb.StringProperty()
    # Excluded fields. If not provided, nothing will be excluded.
    exclude_fields = ndb.StringProperty()
    # Limit the number of results to this.
    limit = ndb.IntegerProperty()


class SimpleRequest(BaseApiModel):
    """Simple request model.

    Usually only one of the variables is used with a request.
    """
    account_id = ndb.IntegerProperty()
    patient_id = ndb.IntegerProperty()


class SimpleResponse(EndpointsModel):
    """Simple response model."""
    success_message = ndb.StringProperty()
