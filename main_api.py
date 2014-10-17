"""This is where we import all the API classes."""

import endpoints

from controllers.api.accounts import AccountsApi


application = endpoints.api_server([
    AccountsApi,
], restricted=False)
