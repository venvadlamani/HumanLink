import services.accounts
import services.exp as exp
import services.jobs
from controllers.api.base import (
    handle_exception,
    humanlink_api,
    get_current_user,
    user_required,
)
from models.api.base import (SimpleRequest, SimpleResponse)
from models.api.jobs import (JobApiModel, SelectApplicantRequest)

from protorpc import remote


@humanlink_api.api_class(resource_name='jobs', path='jobs')
class JobsApi(remote.Service):

    @SimpleRequest.method(name='get', path='{job_id}', http_method='GET',
                          request_fields=('job_id',),
                          response_message=JobApiModel.ProtoModel())
    @user_required
    def get(self, req):
        """Retrieve job details.

        :param req.job_id: (int) ID of the job to retrieve.
        """
        job_id = req.job_id
        try:
            account = get_current_user()
            job_dto = services.jobs.get_by_id(account.id, job_id)
            api_model = JobApiModel.from_job_dto(job_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='posted', path='posted', http_method='GET',
                          request_fields=(),
                          response_message=JobApiModel.ProtoCollection())
    @user_required
    def posted(self, req):
        """Retrieve jobs posted by the current account."""
        try:
            account = get_current_user()
            job_dtos = services.jobs.posted_jobs(account.id)
            api_models = [JobApiModel.from_job_dto(j) for j in job_dtos]
            return JobApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='selected', path='selected', http_method='GET',
                          request_fields=(),
                          response_message=JobApiModel.ProtoCollection())
    @user_required
    def selected(self, req):
        """Retrieve jobs which the current account was selected for."""
        try:
            account = get_current_user()
            job_dtos = services.jobs.selected_jobs(account.id)
            api_models = [JobApiModel.from_job_dto(j) for j in job_dtos]
            return JobApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='applied', path='applied', http_method='GET',
                          request_fields=(),
                          response_message=JobApiModel.ProtoCollection())
    @user_required
    def applied(self, req):
        """Retrieve jobs for which the current account applied."""
        try:
            account = get_current_user()
            job_dtos = services.jobs.applied_jobs(account.id)
            api_models = [JobApiModel.from_job_dto(j) for j in job_dtos]
            return JobApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='nearby', path='nearby', http_method='GET',
                          request_fields=(),
                          response_message=JobApiModel.ProtoCollection())
    @user_required
    def nearby(self, req):
        """Retrieve jobs nearby the current account."""
        try:
            account = get_current_user()
            job_dtos = services.jobs.nearby_jobs(account.id)
            api_models = [JobApiModel.from_job_dto(j) for j in job_dtos]
            return JobApiModel.ProtoCollection()(items=api_models)
        except exp.ServiceExp as e:
            handle_exception(e)

    @JobApiModel.method(name='update', path='update', http_method='POST',
                        response_message=JobApiModel.ProtoModel())
    @user_required
    def update(self, req):
        """Create or update a job."""
        try:
            account = get_current_user()
            job_dto = JobApiModel.to_job_dto(req)
            if job_dto.id is not None:
                job_dto = services.jobs.update_job(account.id, job_dto)
            else:
                job_dto = services.jobs.create_job(account.id, job_dto)
            api_model = JobApiModel.from_job_dto(job_dto)
            return api_model
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='apply', path='apply', http_method='POST',
                          request_fields=('job_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def apply(self, req):
        """Apply for a job.

        :param req.job_id: (int) ID of the job.
        """
        resp = SimpleResponse()
        job_id = req.job_id
        try:
            account = get_current_user()
            services.jobs.apply_job(account.id, job_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)

    @SelectApplicantRequest.method(name='select_applicant',
                                   path='select_applicant', http_method='POST',
                                   response_message=SimpleResponse.ProtoModel())
    @user_required
    def select_applicant(self, req):
        """Select an applicant for the job."""
        resp = SimpleResponse()
        job_id, caregiver_id = req.job_id, req.caregiver_id
        try:
            account = get_current_user()
            services.jobs.select_applicant(account.id, job_id, caregiver_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)

    @SimpleRequest.method(name='cancel', path='cancel', http_method='POST',
                          request_fields=('job_id',),
                          response_message=SimpleResponse.ProtoModel())
    @user_required
    def cancel(self, req):
        """Cancel a job.

        :param req.job_id: (int) ID of the job.
        """
        resp = SimpleResponse()
        job_id = req.job_id
        try:
            account = get_current_user()
            services.jobs.cancel_job(account.id, job_id)
            return resp.ToMessage()
        except exp.ServiceExp as e:
            handle_exception(e)
