'''
Created on May 27, 2014

@author: Venkatesh
'''
import cgi
import webapp2
import os
import jinja2
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
import json


# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

DEFAULT_USER_NAME = 'default_user'

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def user_key(user_name=DEFAULT_USER_NAME):
    """Constructs a Datastore key for a jobs entity with guestbook_name."""
    return ndb.Key('UserName', user_name)

class Job(ndb.Model):
    """Models an individual Guestbook entry."""
    userid = ndb.StringProperty()
    title = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False) 
    startDate = ndb.DateTimeProperty(indexed=False)   
    date = ndb.DateTimeProperty(auto_now_add=True)

class payorMainPage(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}   
            template = JINJA_ENVIRONMENT.get_template('payorMain.html')
            self.response.write(template.render(variable))     
        else:
             self.redirect(users.create_login_url(self.request.uri))
                             


class payorCreateJob(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
                
        if user:            
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('payorJob.html')
            self.response.write(template.render(variable))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    
             
                
    def post(self):
    
        user = users.get_current_user()
        # We set the parent key on each 'Greeting' to ensure each guestbook's
        # greetings are in the same entity group.
        
        if user:  
            logging.error('creating a job in the database')    
            job = Job()
                  
            job.userid = user.user_id()          
            job.title = self.request.get('title')
            job.description = self.request.get('description')
            
            logging.error(job.userid)   
            logging.error(job.title ) 
            logging.error(job.description )              
            job.put()    
            
class payorActiveJobs(webapp2.RequestHandler):
    def get(self):
        
        user = users.get_current_user()
        j = Job.query(Job.userid == user.user_id())   
        
        if user:            
            template_values = {'user':user,
                               'activeJobs': j,
                               }
            template = JINJA_ENVIRONMENT.get_template('payorActiveJobs.html')
            self.response.write(template.render(template_values))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    
                    
    def post(self):
        
        user = users.get_current_user()
        j = Job.query(Job.userid == user.user_id())   
        
        if user:            
            template_values = {'user':user,
                               'activeJobs': j,
                               }
            template = JINJA_ENVIRONMENT.get_template('payorActiveJobs.html')
            self.response.write(template.render(template_values))     
        else:
            self.redirect(users.create_login_url(self.request.uri))    
