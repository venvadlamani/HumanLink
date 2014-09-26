'''
Created on Aug 16, 2014

@author: venkatesh
'''

from google.appengine.ext import ndb
from google.appengine.api import users

class Job(ndb.Model):
    """Models an individual PERSON  entry.""" 
    createdBy = ndb.StringProperty()
    title = ndb.StringProperty()
    Description = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
