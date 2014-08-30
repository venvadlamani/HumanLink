from google.appengine.api import users
from google.appengine.api import oauth
import webapp2
from webapp2_extras import sessions
import jinja2
import logging


# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader('templates/'),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])
# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'care-tiger:ctinstance1'


class Admin (webapp2.RequestHandler):
    def get(self):
            user = oauth.get_current_user()            
            template = JINJA_ENVIRONMENT.get_template('admin.html')        
            self.response.write(template.render())
                
class Login (webapp2.RequestHandler):
    def get(self): 
        
        user = users.get_current_user()   
        if user:
            variable = {'user':user}
            template = JINJA_ENVIRONMENT.get_template('profileNewsFeed.html')        
            self.response.write(template.render(variable))  
        else:
            self.redirect(users.create_login_url('/login'))

class Logout (webapp2.RequestHandler):
    def get(self):
        #create the JINJA template       
        template = JINJA_ENVIRONMENT.get_template('splash.html')        
        self.response.write(template.render())
            
class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
    # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()
    
        # To set a value:
        self.session['foo'] = 'bar'
        
        # To get a value:
        foo = self.session.get('foo')    
