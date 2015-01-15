import services.asserts as asserts
import services.email
import services.exp as exp
from models.kinds.accounts import (
    Account,
    Caregiver,
    Patient,
)
from models.kinds.connections import ConnList
from models.kinds.structs import AccountType
from models.dto.accounts import (
    AccountDto,
    CaregiverDto,
    PatientDto,
)

import logging
from google.appengine.ext import ndb


def create_account(email, password_raw, account_type, auth_id_pre='local:',
                   _dto=True):
    """Creates a new account. Sends an email confirmation.

    :param email: (str) Email address.
    :param password_raw: (str) Raw password.
    :param auth_id_pre: (str) Auth ID prefix.
    :return: The newly created account.
            (dto.accounts.AccountDto) if _dto is True
            (kinds.accounts.Account) if _dto is False
    """
    asserts.type_of(email, basestring)
    asserts.type_of(password_raw, basestring)
    asserts.type_of(account_type, AccountType)

    email = email.lower()
    auth_id = auth_id_pre + email

    account = _create_new_account(email, password_raw, auth_id)
    _account_setup(account_type, account)

    # Async email.
    # Uncomment once the SSL issue is fixed.
    # services.email.send_email_verification(account.id)
    if not _dto:
        return account
    return AccountDto.from_account_ndb(account)


def login(email, password_raw, auth_id_pre='local:'):
    """Checks if given credentials are valid.

    :param email: (str) Email address.
    :param password_raw: (str) Raw password.
    :param auth_id_pre: (str) Auth ID prefix.
    :return: (dto.accounts.AccountDto) or (None)
    """
    asserts.type_of(email, basestring)
    asserts.type_of(password_raw, basestring)

    email = email.lower()
    auth_id = auth_id_pre + email
    account = Account.get_by_auth_password(auth_id, password_raw)
    return AccountDto.from_account_ndb(account)


def account_by_id(account_id, _dto=True):
    """Returns the account associated with the given account_id.

    :param account_id: (int) ID of the account.
    :return: (dto.accounts.AccountDto) if _dto is True
             (kinds.accounts.Account) if _dto is False
             (None) if account does not exist.
    """
    asserts.valid_id_type(account_id)

    account = Account.get_by_id(account_id)
    if account is None:
        logging.warning('account not found. id={}'.format(account_id))
    if not _dto:
        return account
    return AccountDto.from_account_ndb(account)


def accounts_by_ids(account_ids):
    """Returns the accounts associated with the given account IDs.

    :param account_ids: (list<int>) List of account IDs.
    :return: (list<kinds.accounts.Account>) List of accounts.
    """
    keys = Account.ids_to_keys(account_ids)
    return ndb.get_multi(keys)


def caregiver_by_account(account_id, _dto=True):
    """Returns the caregiver details that belongs to the given account_id.

    :param account_id: (int) ID of the account.
    :return: (dto.accounts.CaregiverDto) if _dto is True
             (kinds.accounts.Caregiver) if _dto is False
             (None) if account or caregiver does not exist.
    """
    asserts.valid_id_type(account_id)

    account = account_by_id(account_id, _dto=False)
    if account is not None:
        if not asserts.is_valid_id_type(account.caregiver_id):
            raise exp.BadRequestExp()
        caregiver = Caregiver.get_by_id(account.caregiver_id)
        if not _dto:
            return caregiver
        return CaregiverDto.from_caregiver_ndb(caregiver)


def caregiver_update(actor_id, caregiver_dto, _dto=True):
    """Updates the caregiver associated to the given account.

    :param actor_id: (int) ID of the account performing the action.
    :param caregiver_dto: (dto.accounts.CaregiverDto) caregiver DTO from
                          request.
    :return: (dto.accounts.CaregiverDto) if _dto is True
             (kinds.accounts.Caregiver) if _dto is False
    """
    caregiver_ndb = caregiver_by_account(actor_id, _dto=False)

    for k in caregiver_dto._props:
        if not hasattr(caregiver_dto, k):
            continue
        v = getattr(caregiver_dto, k)
        if v is not None:
            setattr(caregiver_ndb, k, v)

    caregiver_ndb.put()
    if not _dto:
        return caregiver_ndb
    return CaregiverDto.from_caregiver_ndb(caregiver_ndb)


def patients_by_account(account_id, _dto=True):
    """Returns the list of patients that belong to the given account_id.

    :param account_id: (int) ID of the account.
    :return: (list<dto.accounts.PatientDto>) if _dto is True
             (list<kinds.accounts.Patient>) if _dto is False
             (None) if account or patients don't exist.
    """
    asserts.valid_id_type(account_id)

    account = account_by_id(account_id)
    if account is not None and account.patient_ids:
        keys = Patient.ids_to_keys(account.patient_ids)
        patients = ndb.get_multi(keys)
        if not _dto:
            return patients
        return [PatientDto.from_patient_ndb(p) for p in patients]


def patient_by_id(actor_id, patient_id, _dto=True):
    """Returns the patient associated with the given account and patient_id.

    :param actor_id: (int) ID of the account performing the action.
    :param patient_id: (int) ID of the patient to retrieve.
    :return: (dto.accounts.PatientDto) if _dto is True
             (kinds.accounts.Patient) if _dto is False
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(patient_id)

    account = account_by_id(actor_id, _dto=False)
    if account is not None:
        if patient_id not in account.patient_ids:
            raise exp.PermissionExp()
        patient = Patient.get_by_id(patient_id)
        if not _dto:
            return patient
        return PatientDto.from_patient_ndb(patient)


def patient_remove(actor_id, patient_id):
    """Removes the given patient_id from the given account.

    :param actor_id: (int) ID of the account performing the action.
    :param patient_id: (int) ID of the patient to be removed.
    :return: (None)
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(patient_id)

    patient = patient_by_id(actor_id, patient_id)
    if patient is not None:
        account = account_by_id(actor_id)
        account.patient_ids.remove(patient_id)
        patient.soft_delete = True
        ndb.put_multi([account, patient])


def patient_update(actor_id, patient_dto, _dto=True):
    """Create or update a single patient from the given account.

    :param actor_id: (int) ID of the account performing the action.
    :param patient_dto: (dto.accounts.PatientDto) patient DTO from request.
    :return: (dto.accounts.PatientDto) if _dto is True
             (kinds.accounts.Patient) if _dto is False
    """
    account_ndb = account_by_id(actor_id, _dto=False)

    if asserts.is_valid_id_type(patient_dto.id):
        patient_ndb = patient_by_id(actor_id, patient_dto.id, _dto=False)
    else:
        patient_ndb = Patient(account_id=actor_id)

    if patient_dto.first is not None:
        patient_ndb.first = patient_dto.first
    if patient_dto.last is not None:
        patient_ndb.last = patient_dto.last
    if patient_dto.phone_number is not None:
        patient_ndb.phone_number = patient_dto.phone_number
    if patient_dto.relationship is not None:
        patient_ndb.relationship = patient_dto.relationship
    if patient_dto.dob is not None:
        patient_ndb.dob = patient_dto.dob
    if patient_dto.gender is not None:
        patient_ndb.gender = patient_dto.gender
    if patient_dto.care_type is not None:
        patient_ndb.care_type = patient_dto.care_type
    if patient_dto.pets is not None:
        patient_ndb.pets = patient_dto.pets
    if patient_dto.caregiver_pref_gender is not None:
        patient_ndb.caregiver_pref_gender = patient_dto.caregiver_pref_gender
    if patient_dto.additional_info is not None:
        patient_ndb.additional_info = patient_dto.additional_info
    if patient_dto.address is not None:
        patient_ndb.address = patient_dto.address

    patient_ndb.put()
    if patient_ndb.id not in account_ndb.patient_ids:
        account_ndb.patient_ids.append(patient_ndb.id)
        account_ndb.put()

    if not _dto:
        return patient_ndb
    return PatientDto.from_patient_ndb(patient_ndb)


def _create_new_account(email, password_raw, auth_id):
    """Performs validation and stores a new account.

    :return: (kinds.accounts.Account)
    """
    # Minimum password length.
    pass_min_len = 6
    if not services.email.is_valid_email(email):
        raise exp.ValueExp('Invalid email.')
    if password_raw[0] == ' ' or password_raw[-1] == ' ':
        raise exp.ValueExp('Password must not start or end white a space.')
    if len(password_raw) < pass_min_len:
        raise exp.ValueExp('Password must be at least {} characters.'
                           .format(pass_min_len))
    success, account = Account.create_user(
        auth_id=auth_id,
        unique_properties=['email'],
        email=email,
        password_raw=password_raw)
    if not success:
        logging.info('Signup failed. email: %s' % email)
        raise exp.BadRequestExp('Signed failed.')
    return account


def _account_setup(account_type, account):
    """Sets up the newly created account.

    TODO(kanat): This step is heavy, consider using a Task Queue.

    :return: (None)
    """
    account.account_type = account_type
    # Connections list.
    connlist = ConnList(account_id=account.id)
    connlist.put()
    account.connlist_id = connlist.id
    # Caregiver details.
    if account_type == AccountType.Caregiver:
        caregiver = Caregiver(account_id=account.id)
        caregiver.put()
        account.caregiver_id = caregiver.id
    account.put()
