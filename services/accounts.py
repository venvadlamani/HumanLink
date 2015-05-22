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
    UserDto,
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
    services.email.send_email_verification(account.id)
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


def account_by_id(account_id, _dto=True, _throw=True):
    """Returns the account associated with the given account_id.

    :param account_id: (int) ID of the account.
    :return: (dto.accounts.AccountDto) if _dto is True.
             (kinds.accounts.Account) if _dto is False.
             (None) if account does not exist.
    :raise: (exp.NotFoundExp) if `_throw` is True and account is not found.
    """
    asserts.valid_id_type(account_id)

    account = Account.get_by_id(account_id)
    if account is None and _throw:
        logging.warning('account not found. id={}'.format(account_id))
        raise exp.NotFoundExp('Account not found.')
    if not _dto:
        return account
    return AccountDto.from_account_ndb(account)


def account_by_email(email, _dto=True):
    """Returns the account associated with the given email address.

    :param email: (int) ID of the account.
    :return: (dto.accounts.AccountDto) if _dto is True.
             (kinds.accounts.Account) if _dto is False.
             (None) if account does not exist.
    """
    asserts.type_of(email, basestring)

    account = Account.query(Account.email == email.lower()).get()
    if account is None:
        logging.warning('account not found. email={}'.format(email))
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


def account_meta(account_id):
    """This is similar to `account_by_id`, except the returned value is UserDto.

    UserDto contains a small subset of basic account information that can be
    used for any general-purpose account related information.

    :param account_id: (int) ID of the account to retrieve.
    :return: (dto.accounts.UserDto)
    """
    account = account_by_id(account_id, _dto=False)
    return UserDto.from_account_ndb(account)


def account_update(actor_id, account_dto, _dto=True):
    """Updates account information.

    :param actor_id: (int) ID of the account.
    :param account_dto: (dto.accounts.AccountDto) DTO with updated information.
    :return: (dto.accounts.AccountDto) if _dto is True.
             (kinds.accounts.Account) if _dto is False.
    """
    asserts.type_of(account_dto, AccountDto)

    ac = account_by_id(actor_id, _dto=False)
    acd = account_dto

    def has_changed(pdto, pndb):
        return pdto is not None and pdto != pndb

    if ac.id != acd.id:
        raise exp.PermissionExp()
    if has_changed(acd.first, ac.first):
        ac.first = acd.first
    if has_changed(acd.last, ac.last):
        ac.last = acd.last
    if has_changed(acd.phone_number, ac.phone_number):
        ac.phone_number = acd.phone_number
    if has_changed(acd.account_type, ac.account_type):
        ac.account_type = acd.account_type
        # First-time caregiver.
        if ac.account_type == AccountType.Caregiver and ac.caregiver_id is None:
            caregiver = Caregiver(account_id=ac.id)
            caregiver.put()
            ac.caregiver_id = caregiver.id
    ac.put()
    if _dto:
        return AccountDto.from_account_ndb(ac)
    return ac


def verify_email(email, token, _dto=True):
    """Verifies the given email verification token.

    :param email: (str) Email address.
    :param token: (str) Verification token.
    :return: Updated account.
    """
    asserts.type_of(email, basestring)
    asserts.type_of(token, basestring)

    account = account_by_email(email, _dto=False)
    if account.verification_token != token:
        raise exp.BadRequestExp('Invalid verification token.')
    if not account.email_verified:
        account.email_verified = True
        account.put()
    if _dto:
        return AccountDto.from_account_ndb(account)
    return account


def caregiver_by_account(account_id, _dto=True):
    """Returns the caregiver details that belongs to the given account_id.

    :param account_id: (int) ID of the account.
    :return: (dto.accounts.CaregiverDto) if _dto is True
             (kinds.accounts.Caregiver) if _dto is False
             (None) if account or caregiver does not exist.
    """
    asserts.valid_id_type(account_id)

    account = account_by_id(account_id, _dto=False)
    if not asserts.is_valid_id_type(account.caregiver_id):
        raise exp.BadRequestExp()
    caregiver = Caregiver.get_by_id(account.caregiver_id)
    if not _dto:
        return caregiver
    return CaregiverDto.from_caregiver_ndb(caregiver)


def caregiver_update(actor_id, caregiver_dto, _dto=True):
    """Updates the caregiver information associated with the given account.

    :param actor_id: (int) ID of the account performing the action.
    :param caregiver_dto: (dto.accounts.CaregiverDto) caregiver DTO from
                          request.
    :return: (dto.accounts.CaregiverDto) if _dto is True
             (kinds.accounts.Caregiver) if _dto is False
    """
    asserts.type_of(caregiver_dto, CaregiverDto)

    cg = caregiver_by_account(actor_id, _dto=False)
    cgd = caregiver_dto

    def has_changed(pdto, pndb):
        return pdto is not None and pdto != pndb

    if has_changed(cgd.zipcode, cg.zipcode):
        cg.zipcode = cgd.zipcode
    if has_changed(cgd.gender, cg.gender):
        cg.gender = cgd.gender
    if has_changed(cgd.dob, cg.dob):
        cg.dob = cgd.dob
    if has_changed(cgd.headline, cg.headline):
        if len(cgd.headline) > 100:
            cgd.headline = cgd.headline[:100]
        cg.headline = cgd.headline
    if has_changed(cgd.bio, cg.bio):
        if len(cgd.bio) > 5000:
            cgd.bio = cgd.bio[:5000]
        cg.bio = cgd.bio

    if has_changed(cgd.care_services, cg.care_services):
        cg.care_services = cgd.care_services
    if has_changed(cgd.gender_preference, cg.gender_preference):
        cg.gender_preference = cgd.gender_preference
    if has_changed(cgd.expertise, cg.expertise):
        cg.expertise = cgd.expertise
    if has_changed(cgd.licenses, cg.licenses):
        cg.licenses = cgd.licenses
    if has_changed(cgd.certifications, cg.certifications):
        cg.certifications = cgd.certifications
    if has_changed(cgd.transportation, cg.transportation):
        cg.transportation = cgd.transportation
    if has_changed(cgd.languages, cg.languages):
        cg.languages = cgd.languages
    if has_changed(cgd.allergies, cg.allergies):
        cg.allergies = cgd.allergies
    if has_changed(cgd.live_in, cg.live_in):
        cg.live_in = cgd.live_in

    cg.put()
    if not _dto:
        return cg
    return CaregiverDto.from_caregiver_ndb(cg)


def patients_by_account(account_id, _dto=True):
    """Returns the list of patients that belong to the given account_id.

    :param account_id: (int) ID of the account.
    :return: (list<dto.accounts.PatientDto>) if _dto is True
             (list<kinds.accounts.Patient>) if _dto is False
             (None) if patients don't exist.
    """
    asserts.valid_id_type(account_id)

    account = account_by_id(account_id, _dto=False)
    if account.patient_ids is not None:
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
    if patient_id not in account.patient_ids:
        raise exp.NotFoundExp('Care recipient not found.')
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

    account = account_by_id(actor_id, _dto=False)
    patient = patient_by_id(account.id, patient_id, _dto=False)
    if patient is not None and patient.id in account.patient_ids:
        account.patient_ids.remove(patient.id)
        patient.soft_delete = True
        ndb.put_multi([account, patient])


def patient_update(actor_id, patient_dto, _dto=True):
    """Creates or updates a single patient for the given account.

    :param actor_id: (int) ID of the account performing the action.
    :param patient_dto: (dto.accounts.PatientDto) patient DTO from request.
    :return: (dto.accounts.PatientDto) if _dto is True
             (kinds.accounts.Patient) if _dto is False
    """
    asserts.type_of(patient_dto, PatientDto)

    def has_changed(pdto, pndb):
        return pdto is not None and pdto != pndb

    account = account_by_id(actor_id, _dto=False)
    if asserts.is_valid_id_type(patient_dto.id):
        patient = patient_by_id(actor_id, patient_dto.id, _dto=False)
    else:
        patient = Patient(account_id=actor_id)

    # Lazily update values.
    # TODO: validate each property individually.
    for p in PatientDto._props:
        pdto = getattr(patient_dto, p, None)
        if has_changed(pdto, getattr(patient, p, None)):
            setattr(patient, p, pdto)

    patient.put()
    if patient.id not in account.patient_ids:
        account.patient_ids.append(patient.id)
        account.put()
    if not _dto:
        return patient
    return PatientDto.from_patient_ndb(patient)


def _create_new_account(email, password_raw, auth_id):
    """Performs validation and stores a new account.

    :return: (kinds.accounts.Account)
    """
    # Minimum password length.
    pass_min_len = 6
    if not services.email.is_valid_email(email):
        raise exp.ValueExp('Invalid email.')
    if password_raw[0] == ' ' or password_raw[-1] == ' ':
        raise exp.ValueExp('Password must not start or end with white a space.')
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
        raise exp.BadRequestExp('The email you entered is already registered.')
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
