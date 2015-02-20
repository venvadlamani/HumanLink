from endpoints_proto_datastore.ndb import EndpointsModel
from endpoints_proto_datastore import utils
from google.appengine.ext import ndb

# Hack. See:
#   https://github.com/GoogleCloudPlatform/endpoints-proto-datastore/issues/83
utils.DATETIME_STRING_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


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
    job_id = ndb.IntegerProperty()


class SimpleResponse(EndpointsModel):
    """Simple response model."""
    success_message = ndb.StringProperty()
