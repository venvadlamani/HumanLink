import services.asserts as asserts
from models.kinds.accounts import Caregiver
from models.kinds.home import CaregiverGeneral
from models.dto import map_props
from models.dto.search import (
    SearchQueryDto,
    SearchResultDto,
    SearchGeneralCaregiverResultDto,
)
from models.api.base import BaseApiModel
from models.api.accounts import UserApiModel
from google.appengine.ext import ndb


class SearchApiModel(BaseApiModel):
    """Search query model."""
    cursor = ndb.StringProperty()
    care_services = Caregiver.care_services
    zipcode = Caregiver.zipcode
    languages = Caregiver.languages
    licenses = Caregiver.licenses
    expertise = Caregiver.expertise
    transportation = Caregiver.transportation
    languages = Caregiver.languages
    gender = Caregiver.gender
    live_in = Caregiver.live_in
    location = ndb.StringProperty()
    care_date = ndb.DateTimeProperty()
    wage_min = ndb.IntegerProperty()
    wage_max = ndb.IntegerProperty()

    @classmethod
    def to_query_dto(cls, search_api):
        """Translates the given SearchApiModel into a SearchQueryDto.

        :param search_api: (api.search.SearchApiModel)
        :return: (dto.search.SearchQueryDto)
        """
        asserts.type_of(search_api, SearchApiModel)

        query_dto = SearchQueryDto()
        map_props(query_dto, search_api, SearchQueryDto._props)
        return query_dto


class SearchResultApiModel(BaseApiModel):
    cursor = ndb.StringProperty()
    user = ndb.StructuredProperty(UserApiModel)
    headline = Caregiver.headline
    wage = ndb.IntegerProperty()
    references = ndb.IntegerProperty()
    rating = ndb.IntegerProperty()
    response_time = ndb.IntegerProperty()

    @classmethod
    def from_result_dto(cls, result_dto):
        """Translates the given SearchResultDto into a
        SearchResultApiModel.

        :param result_dto: (dto.search.SearchResultDto)
        :return (api.search.SearchResultApiModel)
        """
        asserts.type_of(result_dto, SearchResultDto)

        result_api = SearchResultApiModel(
            user=UserApiModel.from_user_dto(result_dto.user)
        )
        map_props(result_api, result_dto, SearchResultDto._props)
        return result_api.ToMessage()


class SearchGeneralCaregiverResultApiModel(BaseApiModel):
    cursor = ndb.StringProperty()
    name = CaregiverGeneral.name
    phone_number = CaregiverGeneral.phone_number
    location = CaregiverGeneral.location

    @classmethod
    def from_result_dto(cls, result_dto):
        """Translates the given SearchGeneralCaregiverResultDto into a
        SearchGeneralCaregiverResultApiModel.

        :param result_dto: (dto.search.SearchGeneralCaregiverResultDto)
        :return (api.search.SearchGeneralCaregiverResultApiModel)
        """
        asserts.type_of(result_dto, SearchGeneralCaregiverResultDto)

        result_api = SearchGeneralCaregiverResultApiModel()

        map_props(result_api, result_dto, SearchGeneralCaregiverResultDto._props)
        return result_api.ToMessage()
