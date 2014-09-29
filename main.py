'''
Created on Apr 21, 2014

@author: Venkatesh
'''
import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp 
from src import splash
from src import login 
from src import signup
from src import admin
from src import payor
from src import test
from src import profile
from src import search
from src import jobs
from src import collections
from src import analytics


#URL ROUTING
jobsTuple = [
#LOGIN AND LOGOUT
             (r'/login', login.Login),
             (r'/logout', login.Logout),
             
#SIGNUP         
             (r'/signUp', signup.MainPage),  
             (r'/signUpSheet', signup.SignUpSheet),               
             (r'/registerInformation', signup.registerInformation),    

#SEARCH             
             (r'/searchResultsAllConnections', search.searchResultsAllConnections),    
             (r'/searchProfilePreview', search.searchProfilePreview),    
             (r'/searchProfilePreviewCaregiver', search.searchProfilePreviewCaregiver),
             (r'/searchProfilePreviewCommunityLeader', search.searchProfilePreviewCommunityLeader),    
             
#PROFILE             
             (r'/profileMainPage', profile.MainPage),         
             (r'/profileViews', profile.profileViews),
             (r'/profileEdit', profile.profileEdit),  
                                                              
             (r'/profilePreviewFranchisee', profile.profilePreviewFranchisee),
             (r'/profilePreviewCaregiver', profile.profilePreviewCaregiver),
             (r'/profilePreviewPatientFamily', profile.profilePreviewPatientFamily),
             (r'/profilePreviewHospital', profile.profilePreviewHospital),
             (r'/profilePreviewFireDepartment', profile.profilePreviewFireDepartment),
             
                         
             (r'/profilePictureForm', profile.profilePictureForm),
             ('/upload', profile.UploadHandler),
             (r'/serve/([^/]+)?', profile.ServeHandler),
             (r'/profileConnections', profile.profileConnections),             
             (r'/profileConnectionsCommunityLeaders', profile.profileConnectionsCommunityLeaders),    
             
             #profile notifications
             (r'/profileNotifications', profile.profileNotifications),
             (r'/profileNotificationsInvitations', profile.profileNotificationsInvitations),
             (r'/profileNotificationsSent', profile.profileNotificationsSent),                          
             (r'/profileNotificationsArchive', profile.profileNotificationsArchive),             
             (r'/profileNotificationsTrash', profile.profileNotificationsTrash),                     
             
#COLLECTIONS             
             (r'/myConnections', collections.myConnections),    
             (r'/collectionsAll', collections.collectionsAll),    
             (r'/collectionsNew', collections.collectionsNew),    

#JOBS             
             (r'/jobsEditJob', jobs.jobsEditJob),    
             (r'/jobsPostJob', jobs.jobsPostJob),    
             
#ANALYTICS 
             (r'/profileSkillsTrends', analytics.profileSkillsTrends),             
             (r'/profileHourlyTrends', analytics.profileHourlyTrends),             
             (r'/profileGeographicTrends', analytics.profileGeographicTrends),             
             (r'/profileSearchTrends', analytics.profileSearchTrends),    

#SPLASH AND CORPORATE
             (r'/', splash.MainPage),
             (r'/mainpagetemp', splash.MainPageTemp),      #temp staging      
             (r'/aboutUs', splash.AboutUsPage),
             (r'/contactUs', splash.ContactUsPage),
             (r'/blog', splash.BlogPage),
             (r'/careers', splash.CareersPage),
             
        
#DATA ADMIN             
             
             (r'/ctadmin', admin.adminPage),
             (r'/ctadminCareers', admin.careersAdminPage),
             (r'/ctadminCareersEdit', admin.careersAdminEditPage),
             (r'/ctadminCareersPost', admin.careersAdminPostPage),                                                                                                                    
             (r'/ctadminBlog', admin.blogAdminMainPage),
             (r'/ctadminBlogEdit', admin.blogAdminEditPage),
             (r'/ctadminBlogPost', admin.blogAdminPostPage),             
             (r'/ctadminContactUs', admin.ContactUsAdminPage),
             (r'/ctadminContactUsEdit', admin.ContactUsEditAdminPage),             
             #Social Worker Pages             
             (r'/ctadminSocialWorker', admin.SocialWorkerAdminPage),             
                          
#Test  Pages                          
             (r'/test', test.MainPage),

             ]

#A dictionary of configuration values for the app. currently just a placeholder for future configs
configDict = {}
configDict['webapp2_extras.sessions'] = {
    'secret_key': 'something-very-very-secret',
}



#application = webapp2.WSGIApplication(routes=jobsTuple, debug=True, config=configDict)


application = webapp2.WSGIApplication([
    webapp2.Route(r'/signup', handler='controllers.accounts.Accounts:signup')
], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()