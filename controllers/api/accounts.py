import services.accounts
import services.exp as exp
from controllers.api.base import (
    handle_exception,
    humanlink_api,
    get_current_user,
    user_required
)
from models.api.accounts import (
    AccountApiModel,
    CaregiverApiModel,
    PatientApiModel,
)
from models.api.base import (SimpleRequest, SimpleResponse)

from protorpc import remote


@humanlink_api.api_class(resource_name='accounts', path='accounts')
class AccountsApi(remote.Service):

    @SimpleRequest.method(name='get', path='{account_id}', http_method='GET',
                          request_fields=('account_id',),
                          response_message=AccountApiModel.ProtoModel())
    @user_required
    def account_get(self, req):
        """Retrieve the account's profile information.

        :param req.account_id: (int) ID of the account to retrieve.
        """
        account_id = req.account_id
        try:
            account_dto = services.accounts.account_by_id(account_id)
            api_model = AccountApiModel.from_account_dto(account_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @AccountApiModel.method(name='update', path='update', http_method='POST',
                            response_message=AccountApiModel.ProtoModel())
    @user_required
    def account_update(self, req):
        """Update account information."""
        raise NotImplementedError('account.update: not implemented')

    @SimpleRequest.method(name='caregiver', path='caregiver', http_method='GET',
                          request_fields=(),
                          response_message=CaregiverApiModel.ProtoModel())
    @user_required
    def caregiver(self, req):
        """Retrieve the account's caregiver details."""
        try:
            account = get_current_user()
            caregiver_dto = services.accounts.caregiver_by_account(account.id)
            api_model = CaregiverApiModel.from_caregiver_dto(caregiver_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @CaregiverApiModel.method(name='caregiver.update', path='caregiver/update',
                              http_method='POST',
                              response_message=CaregiverApiModel.ProtoModel())
    @user_required
    def caregiver_update(self, req):
        """Update the account's caregiver details."""
        try:
            account = get_current_user()
            caregiver_dto = CaregiverApiModel.to_caregiver_dto(req)
            caregiver_dto = services.accounts.caregiver_update(account.id,
                                                               caregiver_dto)
            api_model = CaregiverApiModel.from_caregiver_dto(caregiver_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='patients.list', path='patients/list',
                          http_method='GET', request_fields=(),
                          response_message=PatientApiModel.ProtoCollection())
    @user_required
    def patients_list(self, req):
        """Retrieve the account's patients."""
        try:
            account = get_current_user()
            patient_dtos = services.accounts.patients_by_account(account.id)
            api_models = [PatientApiModel.from_patient_dto(p)
                          for p in patient_dtos]
            return PatientApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='patients.get', path='patients/{patient_id}',
                          http_method='GET', request_fields=('patient_id',),
                          response_message=PatientApiModel.ProtoModel())
    @user_required
    def patients_get(self, req):
        """Retrieve a patient by ID.

        :param req.patient_id: (int) ID of the patient to retrieve.
        """
        patient_id = req.patient_id
        try:
            account = get_current_user()
            patient_dto = services.accounts.patient_by_id(account.id,
                                                          patient_id)
            api_model = PatientApiModel.from_patient_dto(patient_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @PatientApiModel.method(name='patients.update', path='patients/update',
                            http_method='POST',
                            response_message=PatientApiModel.ProtoModel())
    @user_required
    def patients_update(self, req):
        """Create or update a single patient."""
        try:
            account = get_current_user()
            patient_dto = PatientApiModel.to_patient_dto(req)
            patient_dto = services.accounts.patient_update(account.id,
                                                           patient_dto)
            api_model = PatientApiModel.from_patient_dto(patient_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='patients.remove', path='patients/remove',
                          http_method='POST', request_fields=('patient_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def patients_remove(self, req):
        """Remove a single patient.

        :param req.patient_id: (int) ID of the patient to remove.
        """
        patient_id = req.patient_id
        resp = SimpleResponse()
        try:
            account_id = get_current_user()
            services.accounts.patient_remove(account_id, patient_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)
