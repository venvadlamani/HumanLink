import webapp2

routes = [
    webapp2.Route(r'/', name='home', methods=['GET'],
                  handler='controllers.home.Home:index'),

    webapp2.Route(r'/accounts', name='accounts_index', methods=['GET'],
                  handler='controllers.accounts.Accounts:index'),

    webapp2.Route(r'/settings', name='settings_index', methods=['GET'],
                  handler='controllers.settings.Settings:index'),

    webapp2.Route(r'/home', name='home_index', methods=['GET'],
                  handler='controllers.home.Home:index'),

    webapp2.Route(r'/login.json', name='login_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_login'),

    webapp2.Route(r'/logout', name='logout', methods=['GET'],
                  handler='controllers.accounts.Accounts:logout'),

    webapp2.Route(r'/signup.json', name='signup_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_signup'),

    webapp2.Route(r'/contact.json', name='contact_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_contact'),

    webapp2.Route(r'/verify', name='verify_email', methods=['GET'],
                  handler='controllers.accounts.Accounts:verify_email'),

    webapp2.Route(r'/accounts/userdata.json', name='userdata', methods=['GET'],
                  handler='controllers.accounts.Accounts:userdata'),

    webapp2.Route(r'/submit_contact', name='submit_contact', methods=['POST'],
                  handler='controllers.home.Home:POST_submit_contact'),

    webapp2.Route(r'/submit_caregiver_general', name='submit_caregiver_general',
                  methods=['POST'],
                  handler='controllers.home.Home:POST_caregiver_general'),

    webapp2.Route(r'/caregiver_general', name='caregiver_general',
                  methods=['GET'],
                  handler='controllers.home.Home:GET_caregiver_general'),

    webapp2.Route(r'/contact', name='contact', methods=['POST'],
                  handler='controllers.home.Home:POST_contact_request'),

    webapp2.Route(r'/caregiver_profile', name='caregiver_profile',
                  methods=['GET'],
                  handler='controllers.home.Home:GET_caregiver_profile'),

    webapp2.Route(r'/search_refined', name='search_refined',
                  methods=['POST'],
                  handler='controllers.home.Home:GET_search_refined'),

    webapp2.Route(r'/get_settings_notifications', name='get_settings_notifications',
                  methods=['GET'],
                  handler='controllers.settings.Settings:GET_notifications'),

    webapp2.Route(r'/post_settings_notifications', name='post_settings_notifications',
                  methods=['POST'],
                  handler='controllers.settings.Settings:POST_notifications'),

    webapp2.Route(r'/queue/slack', name='slack', methods=['POST'],
                  handler='controllers.tqueue.QueueHandler:slack'),
]
