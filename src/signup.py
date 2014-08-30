'''
Created on Apr 21, 2014

@author: Venkatesh
'''
import webapp2
import jinja2
import logging

from google.appengine.api import users
from google.appengine.ext import ndb


# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])


class Person(ndb.Model):
    """Models an individual PERSON  entry.""" 
    FirstName = ndb.StringProperty()
    LastName = ndb.StringProperty()    
    MobileNumber = ndb.StringProperty()
    Email = ndb.StringProperty()
    NickName = ndb.StringProperty()
    User = ndb.UserProperty()
    profilePictureID = ndb.BlobKeyProperty()    
    date = ndb.DateTimeProperty(auto_now_add=True)

    
class MainPage(webapp2.RequestHandler):
    def get(self):      
        self.redirect(users.create_login_url('/profileMainPage'))        
            

class SignUpSheet(webapp2.RequestHandler):
    def get(self):    
        user = users.get_current_user()                           
        variable = {'user':user} 
        
        template = JINJA_ENVIRONMENT.get_template('signup.html')        
        self.response.write(template.render(variable))   
        

class registerInformation(webapp2.RequestHandler):
    def post(self):        

        user = users.get_current_user()       
                
        p = Person()
         
        p.FirstName = self.request.get('inputFirstName')
        p.LastName = self.request.get('inputLastName')
        p.MobileNumber = self.request.get('inputMobileNumber')
        p.Email = user.email()
        p.NickName = self.request.get('inputNickName') 
        p.User = user
        
        logging.error( p.FirstName)
        logging.error( p.LastName)
        logging.error( p.MobileNumber)  
        logging.error( p.NickName)      
        
        p.put()
        
        logging.error('registerInformation')
        
        self.redirect("/profileMainPage?")
