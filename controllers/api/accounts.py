from controllers.api.base import humanlink_api
from controllers.api.base import get_current_user
from controllers.api.base import user_required
from models.api.accounts import ProfileApiModel
from services import accounts as account_service

from protorpc import remote


@humanlink_api.api_class(resource_name='accounts')
class AccountsApi(remote.Service):

    @ProfileApiModel.method(name='profile.create', http_method='POST',
                            path='accounts/profile/create',
                            request_fields=('first', 'last', 'phone_number',))
    @user_required
    def create_profile(self, profile_api):
        """Create a new profile with the given information."""
        user = get_current_user()
        profile_dto = ProfileApiModel.to_profile_dto(profile_api)
        profile_dto = account_service.create_pofile(user.id, profile_dto)
        return ProfileApiModel.from_profile_dto(profile_dto)

    @ProfileApiModel.method(name='profile.remove', http_method='POST',
                            path='accounts/profile/remove',
                            request_fields=('id',),
                            response_fields=())
    @user_required
    def remove_profile(self, profile_api):
        """Remove the given profile."""
        user = get_current_user()
        account_service.delete_profile(user.id, profile_api.id)
        return profile_api

    @ProfileApiModel.method(name='profile.get', http_method='GET',
                            path='accounts/profile/{id}',
                            request_fields=('id',))
    def get_profile(self, profile_api):
        """Get profile details for the given profile."""
        profile_dto = account_service.profile_by_id(profile_api.id)
        return ProfileApiModel.from_profile_dto(profile_dto)
