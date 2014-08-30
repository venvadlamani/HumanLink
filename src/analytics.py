'''
Created on May 27, 2014

@author: Venkatesh
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
from model.PersonModel import Person
from model.JobModel import Job


# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'care-tiger:ctinstance1'

class profileSkillsTrends(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileSkillsTrends.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))   
            
            
            

class profileGeographicTrends(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileGeographicTrends.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profileSearchTrends(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileSearchTrends.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profileHourlyTrends(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileHourlyTrends.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    