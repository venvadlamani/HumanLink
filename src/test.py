'''
Created on Aug 4, 2014

@author: venkatesh
'''
import webapp2
import jinja2
import logging
import urllib
from google.appengine.api import images
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore

# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

class Person(ndb.Model):
    """Models an individual PERSON  entry."""
    Name = ndb.StringProperty()
    MobileNumber = ndb.StringProperty()
    Email = ndb.StringProperty()
    ProfilePicture = ndb.BlobProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
    def get(self):                

        #persons_query = 
        #persons = persons_query.fetch(10)
        
        person = Person.get_by_id(6015428115562496)
        img = images.Image(Person.ProfilePicture)
        
        logging.error(person.Name)   
        logging.error(person.MobileNumber ) 
        logging.error(person.Email)          
        logging.error(person.ProfilePicture)
                       
        #prepare the dict for passing to the presentation layer
        variable = {'person':person, 'image':img}  
        #create the JINJA template
        #template = JINJA_ENVIRONMENT.get_template('test.html')
        #self.response.write(template.render(variable))
        if (img) :
            self.response.headers['Content-Type'] = 'image/jpeg'
            self.response.out.write(person.ProfilePicture)
        else :
            self.redirect('/static/noimage.jpg')
             