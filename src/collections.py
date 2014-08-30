'''
Created on Aug 17, 2014

@author: venkatesh
'''
import cgi
import webapp2
import os
import jinja2
import logging
import urllib
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import json


# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'care-tiger:ctinstance1'

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

class myConnections(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()       
               
        if user:            
            variable = {'user':user}   
            template = JINJA_ENVIRONMENT.get_template('myConnections.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))

class collectionsAll(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()       
               
        if user:            
            variable = {'user':user}   
            template = JINJA_ENVIRONMENT.get_template('collectionsAll.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))


class collectionsNew(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()       
               
        if user:            
            variable = {'user':user}   
            template = JINJA_ENVIRONMENT.get_template('collectionsNew.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))             
