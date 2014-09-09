'''
Created on May 13, 2014

@author: Venkatesh
'''
import webapp2
import jinja2
import logging
import sys
import os
import json
import cgi
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from pprint import pprint

# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])
# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'care-tiger:ctinstance1'

class adminPage(webapp2.RequestHandler):
    def get(self):
        
        if self.request.get('fmt') == 'json':
            data = {'name' : 'sam', 'age': 3245345}
            self.response.headers['content-type'] = 'text/json'
            self.response.write(json.dumps(data))
            return
    
        self.templateValues = {}
        self.templateValues['title'] = 'AJAX JSON'
        
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('admin.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(self.templateValues))

    def post(self):
        jsonstring = self.request.body
        jsonobject = json.loads(jsonstring)
        
        #print the JSON object to the terminal
        logging.error(pprint(jsonobject))
        logging.error(jsonobject['firstname'])
        logging.error(jsonobject['project']['id'])
        

#CAREERS =========================================================================        
class careersAdminPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('maintenanceCareers.html')        
        self.response.write(template.render(variable))

class careersAdminEditPage(webapp2.RequestHandler):
    def get(self):
        careerList = []

        user = users.get_current_user()
        variable = {'user':user, 'careerList': careerList}   
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('maintenanceCareersEditJob.html')        
        self.response.write(template.render(variable))

class careersAdminPostPage(webapp2.RequestHandler):
    def get(self):
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('maintenanceCareersPostJob.html')        
        self.response.write(template.render())

    def post(self):
        jobTitle = self.request.get('inputJobTitle')
        jobCreator = self.request.get('inputCreator')
        responsibilities = self.request.get('inputResponsibilities')
        qualifications = self.request.get('inputQualifications')
        
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('maintenanceCareers.html')        
        self.response.write(template.render())

#BLOG =============================================================================
class Blog(ndb.Model):
    """Models an individual Guestbook entry."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class blogAdminMainPage(webapp2.RequestHandler):
    def get(self):
        u = users.get_current_user()    
        
        variable = {'user':u}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('adminBlog.html')        
        self.response.write(template.render(variable))

class blogAdminEditPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('adminBlogEdit.html')        
        self.response.write(template.render(variable))

class blogAdminPostPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('adminBlogPost.html')        
        self.response.write(template.render(variable))


#CONTACT US ==========================================================================         
class ContactUsAdminPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('maintenanceContactUs.html')        
        self.response.write(template.render(variable))
        
class ContactUsEditAdminPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('maintenanceContactUsEdit.html')        
        self.response.write(template.render(variable))


#SOCIAL WORKER ==========================================================================         
class SocialWorkerAdminPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('adminSocialWorkerMain.html')        
        self.response.write(template.render(variable))
        