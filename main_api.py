"""This is where we import all the API classes."""

import endpoints

from controllers.api.accounts import AccountsApi
from controllers.api.connections import ConnectionsApi
from controllers.api.jobs import JobsApi
from controllers.api.messages import MessagesApi


application = endpoints.api_server([
    AccountsApi,
    ConnectionsApi,
    JobsApi,
    MessagesApi
], restricted=False)
