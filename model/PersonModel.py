'''
Created on Aug 16, 2014

@author: venkatesh
'''

from google.appengine.ext import ndb
from google.appengine.api import users


class Person(ndb.Model):
    """Models an individual PERSON  entry.""" 
    User = ndb.UserProperty()
    FirstName = ndb.StringProperty()
    LastName = ndb.StringProperty()    
    MobileNumber = ndb.StringProperty()
    Email = ndb.StringProperty()
    profilePictureID = ndb.BlobKeyProperty()
    NickName = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
