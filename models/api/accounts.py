import services.asserts as asserts
from models.kinds.accounts import (
    Account,
    Caregiver,
    Patient,
)
from models.dto import map_props
from models.dto.accounts import (
    AccountDto,
    CaregiverDto,
    PatientDto,
    UserDto,
)
from models.api.base import BaseApiModel

from google.appengine.ext import ndb


class AccountApiModel(BaseApiModel):
    """Represents an account's profile information."""
    id = ndb.IntegerProperty()
    created = Account.created
    created._required = False
    email = Account.email
    email._required = False
    email_verified = Account.email_verified
    first = Account.first
    last = Account.last
    account_type = Account.account_type
    fbid = Account.fbid
    phone_number = Account.phone_number
    phone_number_verified = Account.phone_number_verified

    @classmethod
    def to_account_dto(cls, account_api):
        """Translates the given AccountApiModel to an AccountDto.

        :param account_api: (api.accounts.AccountApiModel)
        :return: (dto.accounts.AccountDto)
        """
        asserts.type_of(account_api, AccountApiModel)

        account_dto = AccountDto()
        map_props(account_dto, account_api, AccountDto._props)
        return account_dto

    @classmethod
    def from_account_dto(cls, account_dto):
        """Translates the given AccountDto to an AccountApiModel.

        :param account_dto: (dto.accounts.AccountDto)
        :return: (api.accounts.AccountApiModel)
        """
        asserts.type_of(account_dto, AccountDto)

        account_api = AccountApiModel()
        map_props(account_api, account_dto, AccountDto._props)
        return account_api.ToMessage()


class UserApiModel(BaseApiModel):
    """Represents a minimal account profile information."""
    account_id = ndb.IntegerProperty()
    first = Account.first
    last = Account.last
    account_type = Account.account_type
    picture_url = ndb.StringProperty()

    @classmethod
    def from_user_dto(cls, user_dto):
        """Translates the given UserDto to a UserApiModel.

        :param user_dto: (dto.accounts.UserDto)
        :return: (api.accounts.UserApiModel)
        """
        asserts.type_of(user_dto, UserDto)

        user_api = UserApiModel()
        map_props(user_api, user_dto, UserDto._props)
        return user_api


class CaregiverApiModel(BaseApiModel):
    """Represents an account's caregiver details."""
    care_services = Caregiver.care_services
    zipcode = Caregiver.zipcode
    gender = Caregiver.gender
    dob = Caregiver.dob
    headline = Caregiver.headline
    bio = Caregiver.bio
    languages = Caregiver.languages
    licenses = Caregiver.licenses
    certifications = Caregiver.certifications
    expertise = Caregiver.expertise
    gender_preference = Caregiver.gender_preference
    allergies = Caregiver.allergies
    transportation = Caregiver.transportation
    live_in = Caregiver.live_in

    @classmethod
    def to_caregiver_dto(cls, caregiver_api):
        """Translates the given CaregiverApiModel to a CaregiverDto.

        :param caregiver_api: (api.accounts.CaregiverApiModel)
        :return: (dto.accounts.CaregiverDto)
        """
        asserts.type_of(caregiver_api, CaregiverApiModel)

        caregiver_dto = CaregiverDto()
        map_props(caregiver_dto, caregiver_api, CaregiverDto._props)
        return caregiver_dto

    @classmethod
    def from_caregiver_dto(cls, caregiver_dto):
        """Translates the given CaregiverDto to a CaregiverApiModel.

        :param caregiver_dto: (dto.accounts.CaregiverDto)
        :return: (api.accounts.CaregiverApiModel)
        """
        asserts.type_of(caregiver_dto, CaregiverDto)

        caregiver_api = CaregiverApiModel()
        map_props(caregiver_api, caregiver_dto, CaregiverDto._props)
        return caregiver_api.ToMessage()


class PatientApiModel(BaseApiModel):
    """Represents a care recipient information."""
    id = ndb.IntegerProperty()
    care_type = Patient.care_type
    prefix = Patient.prefix
    first = Patient.first
    last = Patient.last
    nickname = Patient.nickname
    relationship = Patient.relationship
    address = Patient.address
    phone_number = Patient.phone_number
    notes = Patient.notes
    age = Patient.age
    pets = Patient.pets
    allergies = Patient.allergies
    hobbies = Patient.hobbies
    caregiver_gender = Patient.caregiver_gender
    caregiver_expertise = Patient.caregiver_expertise

    @classmethod
    def to_patient_dto(cls, patient_api):
        """Translates the given PatientApiModel to a PatientDto.

        :param patient_api: (api.accounts.PatientApiModel)
        :return: (dto.accounts.PatientDto)
        """
        asserts.type_of(patient_api, PatientApiModel)

        patient_dto = PatientDto()
        map_props(patient_dto, patient_api, PatientDto._props)
        return patient_dto

    @classmethod
    def from_patient_dto(cls, patient_dto):
        """Translates the given PatientDto to a PatientApiModel.

        :param patient_dto: (dto.accounts.PatientDto)
        :return: (api.accounts.PatientApiModel)
        """
        asserts.type_of(patient_dto, PatientDto)

        patient_api = PatientApiModel()
        map_props(patient_api, patient_dto, PatientDto._props)
        return patient_api.ToMessage()
