import services.asserts as asserts

from models.kinds.jobs import Job, JobApps
from models.dto import map_props
from models.dto.jobs import JobDto
from models.api.base import BaseApiModel


from google.appengine.ext import ndb


class JobApiModel(BaseApiModel):
    """Represents job details.

    `selected_applicant` and `applicants` are only populated
    when the job owner makes a request.
    """
    id = ndb.IntegerProperty()
    account_id = ndb.IntegerProperty()
    patient_id = ndb.IntegerProperty()
    status = Job.status
    start_date = Job.start_date
    end_date = Job.end_date
    audience = Job.audience
    care_types = Job.care_types
    recommended_wage = Job.recommended_wage
    wage = Job.wage
    additional_info = Job.additional_info
    views = ndb.IntegerProperty()
    selected_applicant = JobApps.selected
    applicants = JobApps.applicants

    @classmethod
    def to_job_dto(cls, job_api):
        """Translates the given JobApiModel to a JobDto.

        :param job_api: (api.jobs.JobApiModel)
        :return: (dto.jobs.JobDto)
        """
        asserts.type_of(job_api, JobApiModel)

        job_dto = JobDto()
        map_props(job_dto, job_api, JobDto._props)
        return job_dto

    @classmethod
    def from_job_dto(cls, job_dto):
        """Translates the given JobDto to an JobApiModel.

        :param job_dto: (dto.jobs.JobDto)
        :return: (api.jobs.JobApiModel)
        """
        asserts.type_of(job_dto, JobDto)

        job_api = JobApiModel()
        map_props(job_api, job_dto, JobDto._props)
        return job_api.ToMessage()


class SelectApplicantRequest(BaseApiModel):
    """Select job applicant request."""
    job_id = ndb.IntegerProperty(required=True)
    caregiver_id = ndb.IntegerProperty(required=True)
