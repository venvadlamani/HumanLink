import services.asserts as asserts
import services.exp as exp
from models.kinds.home import (
    ContactUs,
    CaregiverGeneral
)

import logging
from google.appengine.ext import ndb


def search_general_caregivers_ndb():
    """Returns ALL general caregivers.

    :return: (list<kinds.home.CaregiverGeneral>)
    """
    logging.info("######################")
    logging.info("services/home.py")
    caregivers = CaregiverGeneral.gql('WHERE location = :1', '').fetch()
    return caregivers
