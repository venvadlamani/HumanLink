import services.asserts as asserts
import services.accounts
from models.kinds.accounts import Caregiver
from models.dto.accounts import UserDto
from models.dto.search import (
    SearchQueryDto,
    SearchResultDto
)
from google.appengine.ext import ndb
from google.appengine.datastore.datastore_query import Cursor


def query(actor_id, query_dto):
    """Retrieves caregivers with given search critieria.

    :param actor_id: (int) ID of the account.
    :param query_dto: (dto.search.SearchQueryDto) search query.
    :return: (list<dto.search.SearchResultDto>) search results.
    """
    asserts.type_of(query_dto, SearchQueryDto)
    cls, qdto = Caregiver, query_dto

    q = cls.query()
    if qdto.zipcode:
        q = q.filter(cls.zipcode == qdto.zipcode)
    if qdto.live_in:
        q = q.filter(cls.live_in == qdto.live_in)
    if qdto.gender:
        q = q.filter(cls.gender == qdto.gender)
    if qdto.care_services:
        nd = [cls.care_services == c for c in qdto.care_services]
        q = q.filter(ndb.AND(*nd))
    if qdto.licenses:
        nd = [cls.licenses == l for l in qdto.licenses]
        q = q.filter(ndb.AND(*nd))
    if qdto.expertise:
        nd = [cls.expertise == e for e in qdto.expertise]
        q = q.filter(ndb.AND(*nd))
    if qdto.transportation:
        nd = [cls.transportation == t for t in qdto.transportation]
        q = q.filter(ndb.AND(*nd))
    if qdto.languages:
        nd = [cls.languages == l for l in qdto.languages]
        q = q.filter(ndb.AND(*nd))
    cursor = Cursor(urlsafe=qdto.cursor) if qdto.cursor is not None else None
    results, cursor, more = q.fetch_page(15, start_cursor=cursor)
    return _build_results_dto(actor_id, results, cursor, more)


def _build_results_dto(actor_id, caregivers, cursor, more):
    account_ids = [c.account_id for c in caregivers]
    accounts = {a.id: a for a in
                services.accounts.accounts_by_ids(account_ids)}
    result_dtos = []
    for c in caregivers:
        account = accounts[c.account_id]
        result_dtos.append(SearchResultDto(
            user=UserDto.from_account_ndb(account),
            cursor=cursor.urlsafe() if more else None,
            headline=c.headline,
            wage=14,
            references=5,
            rating=4,
            response_time=90
        ))
    return result_dtos