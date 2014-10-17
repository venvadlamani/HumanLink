'''
Created on Apr 21, 2014

@author: Venkatesh
'''
import webapp2
import jinja2
from google.appengine.api import users

from models.kinds.contacts import ContactUs


# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'care-tiger:ctinstance1'


class MainPage(webapp2.RequestHandler):
    def get(self):         
        #get the current user and create local user variable 
        user = users.get_current_user()
        variable = {'user':user}     
        
        #create the JINJA template    
        if user :   
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileNewsFeed.html')        
            self.response.write(template.render(variable))          

        else :
            template = JINJA_ENVIRONMENT.get_template('landingPage.html')        
            self.response.write(template.render(variable))

class MainPageTemp(webapp2.RequestHandler):
    def get(self):         
        #get the current user and create local user variable 
        user = users.get_current_user()
        variable = {'user':user}     
        
        #create the JINJA template    
        if user :   
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileMainPage.html')        
            self.response.write(template.render(variable))          

        else :
            template = JINJA_ENVIRONMENT.get_template('splash.html')        
            self.response.write(template.render(variable))

    
class LaunchPage(webapp2.RequestHandler):
    def get(self):
        
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('franchiseeProfile.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))

class AboutUsPage(webapp2.RequestHandler):
    def get(self):
        
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('aboutus.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))
        
class BlogPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('blog.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))
        
class ContactUsPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('contactus.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))
      
    def post(self):

        
        ct = ContactUs()
        ct.firstName = self.request.get('inputFirstName')
        ct.lastName = self.request.get('inputLastName')
        ct.email= self.request.get('inputEmail')
        ct.phoneNumber= self.request.get('inputPhone')
        ct.questions = self.request.get('inputComment')
        ct.company = self.request.get('inputComment')
        ct.put()
        
                  
        template = JINJA_ENVIRONMENT.get_template('contactUsResponse.html')
        self.response.write(template.render())                
  
        
class CareersPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('careers.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))

class CaregiverBenefitsPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('benefitsCaregivers.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))

class SocialWorkerBenefitsPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('benefitsSocialWorker.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))

class EldersBenefitsPage(webapp2.RequestHandler):
    def get(self):
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('benefitsElders.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))
