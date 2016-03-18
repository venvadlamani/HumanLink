import webapp2

routes = [
    # Routes for the Home module ----------------------------
    webapp2.Route(r'/', name='home', methods=['GET'],
                  handler='controllers.home.Home:index'),

    webapp2.Route(r'/home', name='home_index', methods=['GET'],
                  handler='controllers.home.Home:index'),

    webapp2.Route(r'/submit_contact', name='submit_contact', methods=['POST'],
                  handler='controllers.home.Home:POST_submit_contact'),

    webapp2.Route(r'/caregiver_profile', name='caregiver_profile',
                  methods=['GET'],
                  handler='controllers.home.Home:GET_caregiver_profile'),

    webapp2.Route(r'/seeker_profile', name='seeker_profile',
                  methods=['GET'],
                  handler='controllers.home.Home:GET_seeker_profile'),

    webapp2.Route(r'/contact', name='contact', methods=['POST'],
                  handler='controllers.home.Home:POST_contact_request'),

    webapp2.Route(r'/search_caregivers', name='search_caregivers',
                  methods=['GET'],
                  handler='controllers.home.Home:GET_caregivers'),

    webapp2.Route(r'/search_seekers', name='search_seekers',
                  methods=['GET'],
                  handler='controllers.home.Home:GET_seekers'),

    # Routes for the Accounts module ----------------------------
    webapp2.Route(r'/accounts', name='accounts_index', methods=['GET'],
                  handler='controllers.accounts.Accounts:index'),

    webapp2.Route(r'/login.json', name='login_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_login'),

    webapp2.Route(r'/logout', name='logout', methods=['GET'],
                  handler='controllers.accounts.Accounts:logout'),

    webapp2.Route(r'/reset', name='reset', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_password_reset'),

    webapp2.Route(r'/reset_password', name='reset_password', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_password_reset_form'),

    webapp2.Route(r'/signup.json', name='signup_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_signup'),

    webapp2.Route(r'/contact.json', name='contact_post', methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_contact'),

    webapp2.Route(r'/verify', name='verify_email', methods=['GET'],
                  handler='controllers.accounts.Accounts:verify_email'),

    webapp2.Route(r'/accounts/userdata.json', name='userdata', methods=['GET'],
                  handler='controllers.accounts.Accounts:userdata'),

    webapp2.Route(r'/get_account_basic', name='get_account_basic',
                  methods=['GET'],
                  handler='controllers.accounts.Accounts:GET_basic'),

    webapp2.Route(r'/post_account_basic', name='post_account_basic',
                  methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_basic'),

    webapp2.Route(r'/get_caregiver_profile', name='get_caregiver_profile',
                  methods=['GET'],
                  handler='controllers.accounts.Accounts:GET_caregiver_profile'),

    webapp2.Route(r'/post_caregiver_profile', name='post_caregiver_profile',
                  methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_caregiver_profile'),

    webapp2.Route(r'/post_seeker_profile', name='post_seeker_profile',
                  methods=['POST'],
                  handler='controllers.accounts.Accounts:POST_seeker_profile'),


    # Routes for the Settings module ----------------------------
    webapp2.Route(r'/settings', name='settings_index', methods=['GET'],
                  handler='controllers.settings.Settings:index'),

    webapp2.Route(r'/get_settings_notifications', name='get_settings_notifications',
                  methods=['GET'],
                  handler='controllers.settings.Settings:GET_notifications'),

    webapp2.Route(r'/post_settings_notifications', name='post_settings_notifications',
                  methods=['POST'],
                  handler='controllers.settings.Settings:POST_notifications'),

    webapp2.Route(r'/get_settings_payments', name='get_settings_payments',
                  methods=['GET'],
                  handler='controllers.settings.Settings:GET_payments'),

    webapp2.Route(r'/post_settings_payments', name='post_settings_payments',
                  methods=['POST'],
                  handler='controllers.settings.Settings:POST_payments'),

    webapp2.Route(r'/post_settings_security', name='post_settings_security',
                  methods=['POST'],
                  handler='controllers.settings.Settings:POST_security'),

    webapp2.Route(r'/queue/slack', name='slack', methods=['POST'],
                  handler='controllers.tqueue.QueueHandler:slack'),

    # Routes for the Dashboard module ----------------------------
    webapp2.Route(r'/dashboard', name='dashboard_index', methods=['GET'],
                  handler='controllers.dashboard.Dashboard:index'),


    # Routes for the Admin module ----------------------------
    webapp2.Route(r'/admin', name='admin_index', methods=['GET'],
                  handler='controllers.admin.Admin:index'),

    webapp2.Route(r'/get_admin_verification', name='get_admin_verification',
                  methods=['GET'],
                  handler='controllers.admin.Admin:GET_admin_verification'),

    webapp2.Route(r'/post_admin_verification', name='post_admin_verification',
                  methods=['POST'],
                  handler='controllers.admin.Admin:POST_admin_verification'),

    webapp2.Route(r'/post_admin_password', name='post_admin_password',
                  methods=['POST'],
                  handler='controllers.admin.Admin:POST_admin_password'),

    webapp2.Route(r'/post_admin_guest_caregiver', name='post_admin_guest_caregiver',
                  methods=['POST'],
                  handler='controllers.admin.Admin:POST_admin_guest_caregiver'),

]
