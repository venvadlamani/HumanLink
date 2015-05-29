import services.exp as exp
import services.search
from controllers.api.base import (
    handle_exception,
    humanlink_api,
    get_current_user,
    user_required,
)
from models.api.search import (
    SearchApiModel,
    SearchResultApiModel
)
from protorpc import remote


@humanlink_api.api_class(resource_name='search', path='search')
class SearchApi(remote.Service):

    query_response = SearchResultApiModel.ProtoCollection()
    @SearchApiModel.method(name='query', path='query', http_method='GET',
                           response_message=query_response)
    @user_required
    def query(self, req):
        """Query for caregivers with search criteria."""
        try:
            account = get_current_user()
            query_dto = SearchApiModel.to_query_dto(req)
            result_dtos = services.search.query(account.id, query_dto)
            api_models = [SearchResultApiModel.from_result_dto(res)
                          for res in result_dtos]
            return SearchResultApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)