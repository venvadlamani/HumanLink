from google.appengine.api import taskqueue
from controllers import base
from models.kinds.structs import AccountType
from models.kinds.home import ContactUs
from models.kinds.accounts import Account
from models.kinds.accounts import Caregiver


class Admin(base.BaseHandler):
    def index(self):
        self.render('admin/index.html')

    def GET_admin_verification(self):
        """Get the verification data of caregvier.
        @params: email of caregiver

        @return: returns a dictionary of caregiver verification records
        """
        requestor_email = self.request.get('account_email')
        cgvr_email = self.request.get('email')
        caregiver_dict = {}

        #only admins can run this functionality
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
            print '--------------------'
            print caregiver_dict
        else:
            self.write_json({'message': 'No admin privileges.'})

        self.write_json(caregiver_dict)

    def POST_admin_verification(self):
        """Update password of user."""
        cgvr_email = self.request_json.get('email')
        acct_qry = Account.query(Account.email == cgvr_email).fetch()

        print '*******************'
        print cgvr_email
        print acct_qry

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
