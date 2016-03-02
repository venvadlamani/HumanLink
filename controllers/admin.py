from controllers import base
from models.kinds.accounts import Account
from models.kinds.accounts import Caregiver
from webapp2_extras import security


class Admin(base.BaseHandler):
    def index(self):
        self.render('admin/index.html')

    def GET_admin_verification(self):
        """Get the verification data of caregiver.
        @params: email of caregiver

        @return: returns a dictionary of caregiver verification records
        """
        requestor_email = self.request.get('account_email')
        cgvr_email = self.request.get('email')
        caregiver_dict = {}

        # only admins can run this functionality
        if requestor_email == 'ven@humanlink.co':
            #   Get caregiver account object
            acct_qry = Account.query(Account.email == cgvr_email).fetch()

            #   Get caregiver verifications
            cgvr_qry = Caregiver.query(
                Caregiver.account_id == acct_qry[0].key.id()).fetch()
            caregiver_dict = {
                'email': cgvr_email,
                'phone_verified': cgvr_qry[0].phone_verified,
                'phone_verified_notes': cgvr_qry[0].phone_verified_notes,
                'background_verified': cgvr_qry[0].background_verified,
                'background_verified_notes': cgvr_qry[0].background_verified_notes,
                'offlineID_verified': cgvr_qry[0].offlineID_verified,
                'offlineID_verified_notes': cgvr_qry[0].offlineID_verified_notes,
            }
        else:
            self.write_json({'message': 'No admin privileges.'})

        self.write_json(caregiver_dict)

    def POST_admin_verification(self):
        """Update verification details of caregiver."""
        cgvr_email = self.request_json.get('email')
        acct_qry = Account.query(Account.email == cgvr_email).fetch()

        #   Get caregiver verifications
        cgvr_qry = Caregiver.query(Caregiver.account_id == acct_qry[0].key.id())

        for cgvr in cgvr_qry:
            cgvr.phone_verified = self.request_json.get('phone_verified')
            cgvr.phone_verified_notes = self.request_json.get('phone_verified_notes')
            cgvr.background_verified = self.request_json.get('background_verified')
            cgvr.background_verified_notes = self.request_json.get(
                'background_verified_notes')
            cgvr.offlineID_verified = self.request_json.get('offlineID_verified')
            cgvr.offlineID_verified_notes = self.request_json.get(
                'offlineID_verified_notes')
            cgvr.put()

        self.write_json({'message': 'Updated'})

    def POST_admin_password(self):
        """Update password of user."""
        email = self.request_json.get('email')
        pwd = self.request_json.get('password')

        acct_qry = Account.query(Account.email == email).fetch()

        for row in acct_qry:
            acct = row.key.get()
            acct.password = security.generate_password_hash(
                self.request_json.get('password'), length=12)
            acct.put()

    def POST_admin_invite(self):
        """Update password of user."""
        email = self.request_json.get('email')

        print '************'
        print email
