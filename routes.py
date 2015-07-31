import webapp2


routes = [
    webapp2.Route(r'/', name='home', methods=['GET'],
                  handler='controllers.home.Home:index'),

    webapp2.Route(r'/accounts', name='accounts_index', methods=['GET'],
                  handler='controllers.accounts.Accounts:index'),

    webapp2.Route(r'/settings', name='settings_index', methods=['GET'],
                  handler='controllers.settings.Settings:index'),

    webapp2.Route(r'/login.json', name='login_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_login'),

    webapp2.Route(r'/logout', name='logout', methods=['GET'],
                  handler='controllers.accounts.Accounts:logout'),

    webapp2.Route(r'/signup.json', name='signup_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_signup'),

    webapp2.Route(r'/verify', name='verify_email', methods=['GET'],
                  handler='controllers.accounts.Accounts:verify_email'),

    webapp2.Route(r'/accounts/userdata.json', name='userdata', methods=['GET'],
                  handler='controllers.accounts.Accounts:userdata'),

    webapp2.Route(r'/submit_contact', name='submit_contact', methods=['POST'],
                  handler='controllers.home.Home:POST_submit_contact'),

    webapp2.Route(r'/terms', name='terms', methods=['GET'],
                  handler='controllers.pages.Pages:terms'),

    webapp2.Route(r'/caregivers', name='caregivers', methods=['GET'],
                  handler='controllers.home.Home:caregivers'),

    webapp2.Route(r'/queue/slack', name='slack', methods=['POST'],
                  handler='controllers.tqueue.QueueHandler:slack'),
]
