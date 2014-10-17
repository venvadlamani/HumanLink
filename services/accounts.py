import logging

from models.dto.accounts import ProfileDto
from models.kinds.accounts import Account
from models.kinds.accounts import Profile

from google.appengine.ext import ndb


def account_by_id(account_id):
    """Returns the account associated with the given account_id.

    :param (int) account_id:
        id of the Account entity.
    """
    assert(type(account_id) == int)
    return Account.get_by_id(account_id)


def profile_by_id(profile_id):
    """Returns the profile associated with the given profile_id.

    :param (int) profile_id:
        id of the Profile entity
    :return:
        (models.dto.ProfileDto) ProfileDto associated with profile_id
        None if Profile not found.
    """
    profile_ndb = _profile_by_id(profile_id)
    return ProfileDto.from_profile_ndb(profile_ndb)


def _profile_by_id(profile_id):
    """See profile_by_id()
    Returns models.ndb.Profile instead.
    """
    assert(type(profile_id) == int)
    return Profile.get_by_id(profile_id)


def profiles_by_account(account_id):
    """Returns a list profiles associated with the given account key.

    :param (int) account_id:
        id of the Account entity.
    """
    assert(type(account_id) == int)
    return Profile.gql(
        'WHERE account_id = :1 AND soft_delete = FALSE', account_id).fetch()


def is_profile_owner(account_id, profile_id):
    """Returns whether the given account is the owner
    of the given profile.

    :param (int) account_id:
        id of the Account entity.
    :param (int) profile_id:
        id of the Profile entity.
    :return:
        True or False.
    """
    assert(type(account_id) == int)

    profile_ndb = _profile_by_id(profile_id)
    if profile_ndb and profile_ndb.account_id == account_id:
        return True
    return False


def delete_profile(actor_id, profile_id):
    """Deletes the profile associates with the given profile key.

    :param (int) actor_id:
        Account ID of the user acting.
    :param (int) profile_id:
        key of the Profile entity.
    :return:
        None
    """
    assert(type(actor_id) == int)

    profile_ndb = _profile_by_id(profile_id)
    if not profile_ndb:
        logging.error('Profile not found. profile_id=%d' % profile_id)
        return
    if profile_ndb.account_id != actor_id:
        logging.error('Permission denied: actor=%d owner=%d'
                      % (actor_id, profile_ndb.account_id))
        return
    profile_ndb.key.delete()


def delete_profiles(actor_id):
    """Deletes ALL the profiles associated with the given account_id.

    :param (int) actor_id:
        Account ID of the user acting.
    :return:
        None
    """
    assert(type(actor_id) == int)

    profiles_ndb = Profile.gql(
        'WHERE account_id = %1', actor_id).fetch(keys_only=True)
    ndb.delete_multi(profiles_ndb)


def create_pofile(actor_id, profile_dto):
    """Creates a new profile for the given account.

    :param (int) actor_id:
        Account ID of the user acting.
    :param (models.dto.ProfileDto) profile_dto:
        ProfileDto with profile information to be created.
    :return  (models.dto.ProfileDto):
        ProfileDto with newly created profile details.
    """
    assert(type(actor_id) == int)
    assert(type(profile_dto) == ProfileDto)

    profile_dto.account_id = actor_id
    profile_ndb = ProfileDto.to_profile_ndb(profile_dto)
    profile_ndb.put()
    return ProfileDto.from_profile_ndb(profile_ndb)


def update_profile(actor_id, profile_dto):
    """Updates the given profile in the datastore.

    :param (int) actor_id:
        Account ID of the user acting.
    :param (models.dto.ProfileDto) profile_dto:
        ProfileDto with profile information to be created.
    :param (models.dt.ProfileDto):
        ProfileDto with updated profile details.
    """
    assert(type(actor_id) == int)
    assert(type(profile_dto) == ProfileDto)

    if not profile_dto.id:
        logging.error('profile_id not provided. ' +
                      'Maybe you need to call create_profile()?')
        return
    if not profile_dto.account_id or profile_dto.account_id != actor_id:
        logging.error('Permission denied: actor=%s, owner=%s'
                      % (actor_id, profile_dto.account_id))
        return
    # Perform this manually so we don't mess up any datastore properties.
    profile_ndb = _profile_by_id(profile_dto.id)
    profile_ndb.populate(first=profile_dto.first,
                         last=profile_dto.last,
                         phone_number=profile_dto.phone_number)
    profile_ndb.put()
    return ProfileDto.from_profile_ndb(profile_ndb)
