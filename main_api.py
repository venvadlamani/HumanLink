"""This is where we import all the API classes."""

import endpoints

from controllers.api.accounts import AccountsApi
from controllers.api.connections import ConnectionsApi


application = endpoints.api_server([
    AccountsApi,
    ConnectionsApi,
], restricted=False)
