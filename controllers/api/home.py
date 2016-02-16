import services.home
import services.exp as exp
import logging

from controllers.api.base import (
    handle_exception,
    humanlink_api
)

from models.api.base import (SimpleRequest, SimpleResponse)
from models.api.search import (
    SearchGeneralCaregiverResultApiModel
)

from protorpc import remote


@humanlink_api.api_class(resource_name='home', path='home')
class HomeApi(remote.Service):
    query_response = SearchGeneralCaregiverResultApiModel.ProtoCollection()

    @SimpleRequest.method(name='search', path='search',
                          http_method='GET',
                          request_fields=(),
                          response_message=query_response)
    def search(self, req):
        """Retrieve search results."""
        logging.info("controllers/api/home.py")
        logging.info(req)

        try:
            search_dto = services.home.search_general_caregivers_ndb()
            api_model = SearchGeneralCaregiverResultApiModel.from_result_dto(search_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)
