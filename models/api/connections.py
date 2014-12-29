import services.asserts as asserts
from models.kinds.accounts import Account
from models.kinds.connections import ConnRequest
from models.dto import map_props
from models.dto.connections import (PendingDto, ConnDto)
from models.api.base import BaseApiModel

from google.appengine.ext import ndb


class PendingConnApiModel(BaseApiModel):
    """Represents a single pending connection."""
    account_id = ndb.IntegerProperty()
    first = Account.first
    last = Account.last
    account_type = Account.account_type
    created = ConnRequest.created
    status = ConnRequest.status
    message = ConnRequest.message

    @classmethod
    def from_conn_dto(cls, pending_dto):
        """Translates the given PendingDto to a PendingConnApiModel.

        :param pending_dto: (dto.connections.PendingDto)
        :return: (api.connections.PendingConnApiModel)
        """
        asserts.type_of(pending_dto, PendingDto)

        pendingconn_api = PendingConnApiModel()
        map_props(pendingconn_api, pending_dto, PendingDto._props)
        return pendingconn_api.ToMessage()


class ConnApiModel(BaseApiModel):
    """Represents a single accepted connection."""
    account_id = ndb.IntegerProperty()
    first = Account.first
    last = Account.last
    account_type = Account.account_type
    is_favorite = ndb.BooleanProperty()
    created = ConnRequest.created
    status = ConnRequest.status
    message = ConnRequest.message

    @classmethod
    def from_conn_dto(cls, conn_dto):
        """Translates the given ConnDto to a ConnApiModel.

        :param conn_dto: (dto.connections.ConnDto)
        :return: (api.connections.ConnApiModel)
        """
        asserts.type_of(conn_dto, ConnDto)

        conn_api = ConnApiModel()
        map_props(conn_api, conn_dto, ConnDto._props)
        return conn_api.ToMessage()
