import services.asserts as asserts
from models.dto import map_props
from models.kinds.jobs import Job


class JobDto(object):

    _props = [
        'id', 'account_id', 'patient_id', 'status', 'start_date', 'end_date',
        'audience', 'care_types', 'recommended_wage', 'wage', 'additional_info',
        'views', 'selected_applicant', 'applicants',
    ]

    @classmethod
    def to_job_ndb(cls, job_dto):
        """Translates the given JobDto to Job.

        :param job_dto: (dto.jobs.JobDto)
        :return: (kinds.jobs.Job)
        """
        asserts.type_of(job_dto, JobDto)

        job_ndb = Job()

        map_props(job_ndb, job_dto, Job._props)
        return job_ndb

    @classmethod
    def from_job_ndb(cls, job_ndb):
        """Translates the given Job to JobDto.

        :param job_ndb: (kinds.jobs.Job)
        :return: (dto.jobs.JobDto)
        """
        asserts.type_of(job_ndb, Job)

        job_dto = JobDto()
        map_props(job_dto, job_ndb, JobDto._props)
        return job_dto
