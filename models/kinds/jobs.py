from models.kinds import base

from endpoints_proto_datastore.ndb import EndpointsModel
from google.appengine.ext import ndb
from google.appengine.ext.ndb import msgprop
from protorpc import messages


class JobApplicant(EndpointsModel):
    """A single job applicant.

    Do not persist this; instead, use in JobApps.
    """
    account_id = ndb.IntegerProperty(required=True)
    message = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now=True)


class JobStatus(messages.Enum):
    """Job status."""
    Open = 0
    Accepted = 1
    Cancelled = 2


class JobAudienceType(messages.Enum):
    """Job audience type. Should be used with JobAudience."""
    Connection = 0
    Favorites = 1
    Community = 2


class JobAudience(EndpointsModel):
    """Job audience."""
    category = msgprop.EnumProperty(JobAudienceType,
                                    default=JobAudienceType.Community)
    values = ndb.IntegerProperty(repeated=True)


class Job(base.Base):
    """Job details."""

    _props = [
        'account_id', 'patient_id', 'status', 'start_date', 'end_date',
        'audience', 'care_types', 'recommended_wage', 'wage', 'additional_info',
    ]

    account_id = ndb.IntegerProperty(required=True)
    patient_id = ndb.IntegerProperty()
    status = msgprop.EnumProperty(JobStatus, default=JobStatus.Open)
    start_date = ndb.DateTimeProperty()
    end_date = ndb.DateTimeProperty()
    audience = ndb.StructuredProperty(JobAudience)
    care_types = ndb.StringProperty(repeated=True)
    recommended_wage = ndb.FloatProperty(indexed=False)
    wage = ndb.FloatProperty(indexed=False)
    additional_info = ndb.TextProperty(indexed=False)
    # jobs.JobInvoice ID.
    invoice_id = ndb.IntegerProperty(indexed=False)
    # jobs.JobApps ID.
    apps_id = ndb.IntegerProperty(indexed=False)

    @property
    def total_minutes(self):
        """Total minutes from start date to end date of the job."""
        return (self.end_date - self.start_date).total_seconds() // 60


class JobApps(base.Base):
    """Job applicants.

    This is created when a job is created.
    """
    job_id = ndb.IntegerProperty(required=True)
    selected = ndb.StructuredProperty(JobApplicant)
    applicants = ndb.StructuredProperty(JobApplicant, repeated=True)

    def add_applicant(self, account_id, message=None):
        """Add a new applicant to the list of applicants.

        NOTE: Does not persist.

        :param account_id: (int) ID of the applicant's account.
        :param message: (str) message of the applicant.
        :return: (None)
        """
        self.applicants.append(
            JobApplicant(account_id=account_id, message=message)
        )

    def find_applicant(self, account_id):
        """Find an applicant by account_id.

        :param account_id: (int) ID of the applicant's account to look for.
        :return: (kinds.jobs.JobApplicant) if the applicant is found.
                 (None) if the applicant is not found.
        """
        for app in self.applicants:
            if app.account_id == account_id:
                return app


class JobInvoice(base.Base):
    """Job invoice.

    This is created when a job owner chooses an applicant.
    """
    job_id = ndb.IntegerProperty(required=True)
    start_date = ndb.DateProperty(indexed=False)
    end_date = ndb.DateProperty(indexed=False)
    additional_info = ndb.TextProperty(indexed=False)
    charge = ndb.FloatProperty(indexed=False)
    # accounts.Payment ID.
    payment_id = ndb.IntegerProperty(indexed=False)

    @property
    def total_minutes(self):
        """Total minutes from start date to end date of the reported invoice."""
        return (self.end_date - self.start_date).total_seconds() // 60
