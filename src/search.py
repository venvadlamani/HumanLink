'''
Created on Aug 13, 2014

@author: venkatesh
'''
import cgi
import webapp2
import os
import jinja2
import logging
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
import json

# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'care-tiger:ctinstance1'

            
class searchResultsAllConnections(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        cityOrZipcode = self.request.get('cityOrZipcode')
        
        variable = {'user':user, 'cityOrZipcode': cityOrZipcode}   
        
        logging.debug("CITY OR ZIPCODE ENTERED %s", str(cityOrZipcode))
        
        template = JINJA_ENVIRONMENT.get_template('searchResultsChild.html')
        self.response.write(template.render(variable))        
        
        #passing JSON data
        #self.response.headers['Content-Type'] = 'application/json'
        #obj = {
        #        'success': 'some var',
        #        'payload': 'some var',                
        #         }
        #self.response.write(json.dumps(obj))

class searchResultsRefined(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        cityOrZipcode = self.request.get('cityOrZipcode')
        
        variable = {'user':user, 'cityOrZipcode': cityOrZipcode}   
        
        logging.debug("CITY OR ZIPCODE ENTERED %s", str(cityOrZipcode))
        
        template = JINJA_ENVIRONMENT.get_template('searchResultsMain.html')
        self.response.write(template.render(variable))  
        
     
class searchProfilePreview(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        cityOrZipcode = self.request.get('cityOrZipcode')
        
        variable = {'user':user, 'cityOrZipcode': cityOrZipcode}   
        
        logging.debug("CITY OR ZIPCODE ENTERED %s", str(cityOrZipcode))
        
        template = JINJA_ENVIRONMENT.get_template('searchProfilePreview.html')
        self.response.write(template.render(variable))        
    
class searchProfilePreviewCaregiver(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        cityOrZipcode = self.request.get('cityOrZipcode')
        
        variable = {'user':user, 'cityOrZipcode': cityOrZipcode}   
        
        logging.debug("CITY OR ZIPCODE ENTERED %s", str(cityOrZipcode))
        
        template = JINJA_ENVIRONMENT.get_template('searchProfilePreviewCaregiver.html')
        self.response.write(template.render(variable))  

class searchProfilePreviewCommunityLeader(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        cityOrZipcode = self.request.get('cityOrZipcode')
        
        variable = {'user':user, 'cityOrZipcode': cityOrZipcode}   
        
        logging.debug("CITY OR ZIPCODE ENTERED %s", str(cityOrZipcode))
        
        template = JINJA_ENVIRONMENT.get_template('searchProfilePreviewCommunityLeader.html')
        self.response.write(template.render(variable))                