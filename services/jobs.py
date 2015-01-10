import services.asserts as asserts
import services.exp as exp
from models.kinds.jobs import (
    Job,
    JobApps,
    JobInvoice,
    JobStatus,
)
from models.dto.jobs import JobDto

import logging
from google.appengine.ext import ndb


def posted_jobs_ndb(account_id):
    """Returns jobs posted by the given account_id.

    :param account_id: (int) ID of the account.
    :return: (list<kinds.jobs.Job>)
    """
    asserts.valid_id_type(account_id)

    jobs = Job.gql('WHERE account_id = :1', account_id).fetch()
    return jobs


def posted_jobs(actor_id):
    """See `posted_jobs_ndb`.

    :param actor_id: (int) ID of the account acting.
    :return: (list<dto.jobs.JobDto>)
    """
    jobs = posted_jobs_ndb(actor_id)
    return [_build_job_dto(actor_id, job) for job in jobs]


def selected_jobs_ndb(account_id):
    """Returns jobs for which the given account_id was selected.

    :param account_id: (int) ID of the account.
    :return: (list<kinds.jobs.Job>)
    """
    asserts.valid_id_type(account_id)

    apps = JobApps.gql('WHERE selected.account_id = :1', account_id)
    return _jobs_from_apps(apps)


def selected_jobs(actor_id):
    """See `selected_jobs_ndb`.

    :param actor_id: (int) ID of the account acting.
    :return: (list<dto.jobs.JobDto>)
    """
    jobs = selected_jobs_ndb(actor_id)
    return [_build_job_dto(actor_id, job) for job in jobs]


def applied_jobs_ndb(account_id):
    """Returns jobs for which the given account_id applied.

    :param account_id: (int) ID of the account.
    :return: (list<kinds.jobs.Job>)
    """
    asserts.valid_id_type(account_id)

    apps = JobApps.gql('WHERE applicants.account_id = :1', account_id)
    return _jobs_from_apps(apps)


def applied_jobs(actor_id):
    """See `applied_jobs_ndb`.

    :param actor_id: (int) ID of the account acting.
    :return: (list<dto.jobs.JobDto>)
    """
    jobs = applied_jobs_ndb(actor_id)
    return [_build_job_dto(actor_id, job) for job in jobs]


def nearby_jobs_ndb(account_id):
    """Returns jobs posted nearby the give account_id.

    NOTE: For now, just returns the list of all open jobs.

    :param account_id: (int) ID of the account.
    :return: (list<kinds.jobs.Job>)
    """
    asserts.valid_id_type(account_id)

    jobs = Job.gql('WHERE status = :1 ORDER BY updated DESC',
                   JobStatus.Open).fetch(limit=25)
    return jobs


def nearby_jobs(actor_id):
    """See `nearby_jobs_ndb`.

    :param actor_id: (int) ID of the account acting.
    :return: (list<dto.jobs.JobDto>)
    """
    jobs = nearby_jobs_ndb(actor_id)
    return [_build_job_dto(actor_id, job) for job in jobs]


def get_by_id_ndb(job_id):
    """Returns the job associated with the given job_id.

    :param job_id: (int) ID of the job.
    :return: (kinds.jobs.Job)
    """
    asserts.valid_id_type(job_id)

    job = Job.get_by_id(job_id)
    if job is None:
        logging.warning('Job not found. id={}'.format(job_id))
        raise exp.NotFoundExp()
    return job


def get_by_id(actor_id, job_id):
    """See `get_by_id_ndb`.

    :param job_id: (int) ID of the job.
    :return: (dto.jobs.JobDto)
    """
    job = get_by_id_ndb(job_id)
    return _build_job_dto(actor_id, job)


def create_job_ndb(account_id, job_dto):
    """Create a new job.

    TODO(kanat): Proper input validation, e.g:
        - valid patient_id?
        - valid start, end dates?
        - valid wage?

    :param account_id: (int) ID of the account for which the job belongs.
    :param job_dto: (dto.jobs.JobDto) job details.
    :return: (kinds.jobs.Job)
    """
    asserts.valid_id_type(account_id)
    asserts.type_of(job_dto, JobDto)

    job = JobDto.to_job_ndb(job_dto)
    job.account_id = account_id
    job.put()
    apps = JobApps(job_id=job.id)
    apps.put()
    job.apps_id = apps.id
    job.put()
    return job


def create_job(actor_id, job_dto):
    """See `create_job_ndb`.

    :param actor_id: (int) ID of the account acting.
    :param job_dto: (dto.jobs.JobDto) job details.
    :return: (dto.jobs.JobDto)
    """
    job = create_job_ndb(actor_id, job_dto)
    return JobDto.from_job_ndb(job)


def update_job_ndb(actor_id, job_dto):
    """Update an existing job.

    :param actor_id: (int) ID of the account acting.
    :param job_dto: (dto.jobs.JobDto) job details.
    :return: (kinds.jobs.Job)
    """
    raise NotImplementedError()


def update_job(actor_id, job_dto):
    """See `update_job_ndb`.

    :param actor_id: (int) ID of the account acting.
    :param job_dto: (dto.jobs.JobDto) job details.
    :return: (dto.jobs.JobDto)
    """
    job = update_job_ndb(actor_id, job_dto)
    return JobDto.from_job_ndb(job)


def apply_job(actor_id, job_id, message=None):
    """Apply for a job.

    TODO(kanat): Notify job owner.

    :param actor_id: (int) ID of the account acting.
    :param job_id: (int) ID of the job applying.
    :param message: (str) Optional message.
    :return: (None)
    """
    asserts.valid_id_type(actor_id)
    asserts.valid_id_type(job_id)

    job = get_by_id_ndb(job_id)
    if job.status != JobStatus.Open:
        raise exp.BadRequestExp('Job is not open.')
    if actor_id == job.account_id:
        raise exp.BadRequestExp('Can\'t apply to own job.')
    apps = _get_applicants(job_id)
    if apps.find_applicant(actor_id) is not None:
        logging.warning('Already applied.')
        return
    apps.add_applicant(actor_id, message)
    apps.put()


def select_applicant(actor_id, job_id, caregiver_id):
    """Select an applicant for the job.

    TODO(kanat): Notify selected applicant.

    :param actor_id: (int) ID of the account acting.
    :param caregiver_id: (int) ID of the job applicant's account.
    :return: (None)
    """
    asserts.valid_id_type(caregiver_id)
    _assert_job_owner(actor_id, job_id)

    job = get_by_id_ndb(job_id)
    if job.status != JobStatus.Open:
        raise exp.BadRequestExp('Job is not open')
    if actor_id == caregiver_id:
        raise exp.BadRequestExp('Can\'t select yourself.')
    apps = _get_applicants(job_id)
    applicant = apps.find_applicant(caregiver_id)
    if applicant is None:
        raise exp.NotFoundExp('Applicant not found.')
    # Set up job invoice.
    invoice = JobInvoice(job_id=job.id,
                         start_date=job.start_date,
                         end_date=job.end_date)
    invoice.put()
    apps.selected = applicant
    job.status = JobStatus.Accepted
    job.invoice_id = invoice.id
    ndb.put_multi([apps, job])


def cancel_job(actor_id, job_id, message=None):
    """Cancel a job. Either caregiver or careseeker can cancel.

    TODO(kanat): If caregiver cancelled:
            - send careseeker with a link to re-post the job.

    :param actor_id: (int) ID of the account acting.
    :param job_id: (int) ID of the job to cancel.
    :param message: (str) Optional message.
    :return: (None)
    """
    job = get_by_id_ndb(job_id)
    func = (_cancel_by_careseeker if job.account_id == actor_id
            else _cancel_by_caregiver)
    func(actor_id, job_id, message)


def _cancel_by_careseeker(actor_id, job_id, message=None):
    """Cancel a job by the careseeker.

    TODO(kanat): Notify caregiver w/ message.

    :return: (None)
    """
    _assert_job_owner(actor_id, job_id)

    job = get_by_id_ndb(job_id)
    if job.status == JobStatus.Cancelled:
        logging.info('Job already cancelled.')
        return
    if job.status == JobStatus.Accepted:
        # Notify caregiver.
        pass
    logging.info('Job cancelled by careseeker. job_id={}'.format(job_id))
    job.status = JobStatus.Cancelled
    job.put()


def _cancel_by_caregiver(actor_id, job_id, message=None):
    """Cancel a job the the selected caregiver.

    TODO(kanat): Notify careseeker.

    :return: (None)
    """
    asserts.valid_id_type(actor_id)

    job = get_by_id_ndb(job_id)
    if job.status == JobStatus.Cancelled:
        logging.info('Job already cancelled.')
        return
    apps = _get_applicants(job.id)
    if apps.selected is None or apps.selected.account_id != actor_id:
        raise exp.PermissionExp()
    logging.info('Job cancelled by caregiver. job_id={}'.format(job_id))
    apps.selected = None
    job.status = JobStatus.Cancelled
    ndb.put_multi([apps, job])


def _assert_job_owner(actor_id, job_id):
    if not _is_job_owner(actor_id, job_id):
        raise exp.PermissionExp()


def _is_job_owner(actor_id, job_id):
    asserts.valid_id_type(actor_id)
    job = get_by_id_ndb(job_id)
    return actor_id == job.account_id


def _get_applicants(job_id):
    """Returns `JobApps` for the given job_id."""
    job = get_by_id_ndb(job_id)
    return JobApps.get_by_id(job.apps_id)


def _jobs_from_apps(apps):
    """Returns Job`s given from list of `JobApps`."""
    job_ids = [app.job_id for app in apps]
    jobs = ndb.get_multi(Job.ids_to_keys(job_ids))
    return jobs


def _build_job_dto(actor_id, job):
    """Build a JobDto. Includes job applicants if job owner is acting.

    :param job_id: (kinds.jobs.Job) The job to build the DTO for.
    :return: (dto.jobs.JobDto)
    """
    job_dto = JobDto.from_job_ndb(job)
    # Constant views count.
    job_dto.views = 123
    if _is_job_owner(actor_id, job.id):
        apps = _get_applicants(job.id)
        job_dto.selected_applicant = apps.selected
        job_dto.applicants = apps.applicants
    return job_dto
