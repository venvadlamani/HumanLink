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
import pprint
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




class MainPage(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()       
               
        if user:            
            variable = {'user':user}   
            template = JINJA_ENVIRONMENT.get_template('profileNewsFeed.html')
            self.response.write(template.render(variable))     
        else:
             self.redirect(users.create_login_url(self.request.uri))
                             
                             
class profileEdit(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileEdit.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))      
   
    def post(self):       
        user = users.get_current_user()
        self.response.out.write("This is a POST Request \n")
        
        #jsonstring = self.request.body
        #jsonobject = json.loads(jsonstring)

        #print the JSON object to the terminal
        #logging.error(pprint(jsonobject))
        #logging.error(jsonobject['firstname'])
        #logging.error(jsonobject['project']['id'])
          
        logging.error("Hello Dolly")

            
class profileViews(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileViews.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

#NOTIFICATIONS
class profileNotifications(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileNotificationsInbox.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profileNotificationsInvitations(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileNotificationsInvitations.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profileNotificationsSent(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileNotificationsSent.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profileNotificationsArchive(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileNotificationsArchive.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profileNotificationsTrash(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileNotificationsTrash.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

################ PROFILE PREVIEW
class profilePreviewFranchisee(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profilePreviewFranchisee.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    
             
class profilePreviewCaregiver(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profilePreviewCaregiver.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    
            
            
class profilePreviewPatientFamily(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profilePreviewPatientFamily.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    


class profilePreviewHospital(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profilePreviewHospital.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profilePreviewFireDepartment(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
               
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profilePreviewFireDepartment.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))                
###############            
class profilePaymentInfo(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profilePaymentInfo.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))   

#COLLECTIONS
class profileConnections(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileConnections.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    

class profileConnectionsCommunityLeaders(webapp2.RequestHandler):
    def get(self):       
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileConnectionsCommunityLeaders.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))  
             
#PROFILE PICTURE            
class profilePictureForm(webapp2.RequestHandler):
    def get(self):      
        user = users.get_current_user()
            
        if user:                        
            upload_url = blobstore.create_upload_url('/upload')              

            variable = {'user':user, 'upload_url': upload_url}
            template = JINJA_ENVIRONMENT.get_template('profilePicture.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))   

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):         
        user = users.get_current_user()
        pQuery = Person.query ()
        upload_files = self.get_uploads('profilePic')         
        blob_info = upload_files[0]
        pQuery.profilePictureID = blob_info.key()
        pQuery.put()
        
        self.redirect('/profilePictureForm')
        #self.redirect('/serve/%s' % blob_info.key())

class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)
