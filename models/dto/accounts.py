import services.asserts as asserts
from models.kinds.accounts import (
    Account,
    Caregiver,
    Patient,
)
from models.dto import map_props


class AccountDto(object):

    _props = [
        'id', 'created', 'email', 'email_verified', 'fbid', 'first', 'last',
        'account_type', 'phone_number', 'phone_number_verified',
    ]

    @classmethod
    def to_account_ndb(cls, account_dto):
        """Translates the given AccountDto to Account NDB model.

        :param account_dto: (dto.accounts.AccountDto)
        :return: (kinds.accounts.Account)
        """
        asserts.type_of(account_dto, AccountDto)

        # For now, the attributes map 1:1. It will not always be the case.
        # For example, convert enum values to enum indices.
        account_ndb = Account()
        map_props(account_ndb, account_dto, cls._props)
        return account_ndb

    @classmethod
    def from_account_ndb(cls, account_ndb):
        """Translates the given Account NDB to AccountDto.

        :param account_ndb: (kinds.accounts.Account)
        :return: (dto.accounts.AccountDto)
        """
        asserts.type_of(account_ndb, Account)

        account_dto = AccountDto()
        map_props(account_dto, account_ndb, cls._props)
        return account_dto


class UserDto(object):
    """UserDto: account metadata.

    UserDto is a general-purpose account related information that is better to
    use when all the information in AccountDto is not necessary.
    """

    _props = ['account_id', 'account_type', 'first', 'last', 'picture_url']

    @classmethod
    def from_account_ndb(cls, account_ndb):
        """Builds a UserDto from the given Account NDB model.

        :param account_ndb:
        :return:
        """
        asserts.type_of(account_ndb, Account)

        user_dto = UserDto()
        map_props(user_dto, account_ndb, cls._props)
        user_dto.account_id = account_ndb.id
        return user_dto


class CaregiverDto(object):

    _props = [
        'gender', 'dob', 'bio', 'languages', 'licenses', 'work_experience',
        'work_experience', 'certifications', 'careservices',
    ]

    @classmethod
    def to_caregiver_ndb(cls, caregiver_dto):
        """Translates the given CaregiverDto to Caregiver NDB model.

        :param caregiver_dto: (dto.accounts.CaregiverDto)
        :return: (kinds.accounts.Caregiver)
        """
        asserts.type_of(caregiver_dto, CaregiverDto)

        caregiver_ndb = Caregiver()
        map_props(caregiver_ndb, caregiver_dto, cls._props)
        return caregiver_ndb

    @classmethod
    def from_caregiver_ndb(cls, caregiver_ndb):
        """Translates the given Caregiver NDB to CaregiverDto.

        :param caregiver_ndb: (kinds.accounts.Caregiver)
        :return: (dto.accounts.CaregiverDto)
        """
        asserts.type_of(caregiver_ndb, Caregiver)

        caregiver_dto = CaregiverDto()
        map_props(caregiver_dto, caregiver_ndb, cls._props)
        return caregiver_dto


class PatientDto(object):

    _props = [
        'id', 'first', 'last', 'phone_number', 'relationship',
        'dob', 'gender', 'pets', 'care_type', 'caregiver_pref_gender',
        'additional_info', 'address',
    ]

    @classmethod
    def to_patient_ndb(cls, patient_dto):
        """Translates the given PatientDto to Patient NDB model.

        :param patient_dto: (dto.accounts.PatientDto)
        :return: (kinds.accounts.Patient)
        """
        asserts.type_of(patient_dto, PatientDto)

        patient_ndb = Patient()
        map_props(patient_ndb, patient_dto, cls._props)
        return patient_ndb

    @classmethod
    def from_patient_ndb(cls, patient_ndb):
        """Translates the given Patient NDB to PatientDto.

        :param patient_ndb: (kinds.accounts.Patient)
        :return: (dto.accounts.PatientDto)
        """
        asserts.type_of(patient_ndb, Patient)

        patient_dto = PatientDto()
        map_props(patient_dto, patient_ndb, cls._props)
        return patient_dto
