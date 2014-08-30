
'''
Created on Mar 25, 2014

@author: Venkatesh
'''
import cgi
import webapp2
import MySQLdb
import os
import jinja2
import logging
from google.appengine.ext import db


# Configure the Jinja2 environment.
JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  autoescape=True,
  extensions=['jinja2.ext.autoescape'])

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'care-tiger:ctinstance1'

class MainPage(webapp2.RequestHandler):
    def get(self):
        # Open a connection to the caretiger database.
        if (os.getenv('SERVER_SOFTWARE') and
            os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
            db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='caretiger', user='root')
        else:
            # Alternately, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root')
            db = MySQLdb.connect(host='173.194.80.3', port=3306, user='root', passwd="minnie", db="caretiger")

        cursor = db.cursor()
        
        #create a list of caregiver type to render with the HTML.
        try:
            cursor.execute('SELECT ID, CARETYPE FROM CARETYPE')
            
            #if cursor execution is successful then create list
            careGiverTypeList = []
            
            for row in cursor.fetchall():
                careGiverTypeList.append(dict ([ ('ID', row[0]),
                                                ('type',cgi.escape(row[1]))                                                                                                
                                                ]))
                
            logging.error('retrieving posts from the datastore')
        except:
            logging.error('There was an error retrieving posts from the datastore')
      
        
        #create the JINJA template
        variable = {'careGiverType': careGiverTypeList}     
        template = JINJA_ENVIRONMENT.get_template('createJob.html')
        self.response.write(template.render(variable))
        #self.response.write(caregivertype_variable)
        #self.response.write(caregiverlist_variable)      
        db.close()
        
class createJob(webapp2.RequestHandler):
    
    def post(self):        
        # Handle the post to create a new JOBS entry.
        careReceiverId = 1 #currently HARDCODE THE USER ID
        careType = self.request.get('careType')
        careDate = self.request.get('careDate')       
        if self.request.get('backGroundVerified') == 'on' :
            backGroundVerified = 1
        else:
            backGroundVerified = 0    
        genderPreference = self.request.get('genderPreference')
        jobDescription = self.request.get('jobDescription')
        

                
        if (os.getenv('SERVER_SOFTWARE') and
            os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
            db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='caretiger', user='root')
        else:
            db = MySQLdb.connect(host='173.194.80.3', port=3306, user='root', passwd="minnie", db="caretiger")
            # Alternately, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root')

        #get a cursor
        cursor = db.cursor()
        try:
            cursor.execute('INSERT INTO JOBS (CARE_RECEIVER_ID, \
                                            CARETYPE, \
                                            CAREDATE, \
                                            BACKGROUND_VERIFIED, \
                                            GENDER_PREFERENCE, \
                                            JOB_DESCRIPTION) \
                                            VALUES (%s, %s, %s, %s, %s, %s)', \
                                            (careReceiverId, 1, careDate, backGroundVerified, genderPreference, jobDescription))
        except:
            logging.error('There was an error INSERTING into the datastore')
            raise

        db.commit()
        db.close()

        #template = JINJA_ENVIRONMENT.get_template('splash.html')
        self.redirect("/")


