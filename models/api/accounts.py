from models.api.base import BaseApiModel
from models.dto.accounts import ProfileDto
from models.kinds.accounts import Account
from models.kinds.accounts import Profile

from google.appengine.ext import ndb


class AccountApiModel(BaseApiModel):
    id = ndb.IntegerProperty()
    email = Account.email
    verified = Account.verified
    soft_delete = Account.soft_delete


class ProfileApiModel(BaseApiModel):
    id = ndb.IntegerProperty()
    account_id = Profile.account_id
    first = Profile.first
    last = Profile.last
    phone_number = Profile.phone_number

    @staticmethod
    def to_profile_dto(profile_api):
        assert(type(profile_api) == ProfileApiModel)
        return ProfileDto(id=profile_api.id,
                          account_id=profile_api.account_id,
                          first=profile_api.first,
                          last=profile_api.last,
                          phone_number=profile_api.phone_number)

    @staticmethod
    def from_profile_dto(profile_dto):
        assert(type(profile_dto) == ProfileDto)
        return ProfileApiModel(id=profile_dto.id,
                               account_id=profile_dto.account_id,
                               first=profile_dto.first,
                               last=profile_dto.last,
                               phone_number=profile_dto.phone_number)
