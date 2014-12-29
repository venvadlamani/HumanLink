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
    address = Account.address

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


class CaregiverApiModel(BaseApiModel):
    """Represents an account's caregiver details."""
    gender = Caregiver.gender
    dob = Caregiver.dob
    bio = Caregiver.bio
    languages = Caregiver.languages
    licenses = Caregiver.licenses
    work_experience = Caregiver.work_experience
    certifications = Caregiver.certifications
    careservices = Caregiver.careservices

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

        caregiver_api = AccountApiModel()
        map_props(caregiver_api, caregiver_dto, CaregiverDto._props)
        return caregiver_api.ToMessage()


class PatientApiModel(BaseApiModel):
    """Represents a patient's information."""
    id = ndb.IntegerProperty()
    first = Patient.first,
    last = Patient.last,
    phone_number = Patient.phone_number
    relationship = Patient.relationship,
    dob = Patient.dob,
    gender = Patient.gender,
    pets = Patient.care_type,
    caregiver_pref_gender = Patient.caregiver_pref_gender,
    additional_info = Patient.additional_info
    address = Patient.address

    @classmethod
    def to_patient_dto(cls, patient_api):
        """Translates the given PatientApiModel to a PatientDto.

        :param patient_api: (api.accounts.PatientApiModel)
        :return: (dto.accounts.PatientDto)
        """
        asserts.type_of(patient_api, PatientApiModel)

        patient_dto = CaregiverDto()
        map_props(patient_dto, patient_api, PatientDto._props)
        return patient_dto

    @classmethod
    def from_patient_dto(cls, patient_dto):
        """Translates the given PatientDto to a PatientApiModel.

        :param patient_dto: (dto.accounts.PatientDto)
        :return: (api.accounts.PatientApiModel)
        """
        asserts.type_of(patient_dto, CaregiverDto)

        patient_api = AccountApiModel()
        map_props(patient_api, patient_dto, PatientDto._props)
        return patient_api.ToMessage()
