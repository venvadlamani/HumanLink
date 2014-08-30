'''
Created on Aug 18, 2014

@author: venkatesh
'''
from google.appengine.ext import ndb
from google.appengine.api import users

class ContactUs(ndb.Model):
    """Models an individual PERSON  entry.""" 
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    email = ndb.StringProperty()
    phoneNumber = ndb.StringProperty()
    company = ndb.StringProperty()
    questions = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)