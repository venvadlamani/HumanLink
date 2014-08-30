'''
Created on May 6, 2014

@author: Venkatesh
'''

import webapp2
import jinja2

# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])


class LaunchPage(webapp2.RequestHandler):
    def get(self):
        
        variable = {}     
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('not_found.html')        
        #logging.error('Loading the Splash.html')
        self.response.write(template.render(variable))