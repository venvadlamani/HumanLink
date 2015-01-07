'use strict';

/**
 * Keeps track of the current logged in user.
 */
angular
    .module('Common')
    .factory('userSession', ['apiService', function (apiService) {

        var self = this;
        self.userdata = null;
        self.ctrlHelper = new HL.CtrlHelper();

        self.setAccount = function(account) {
            self.userdata = account;
        };

        self.unsetAccount = function() {
            self.userdata = null;
        };

        self.isAuthorized = function() {
            return self.userdata !== null;
        };

        self.update = function() {
            self.ctrlHelper.success = function (data, status, headers, config) {
                self.userdata = data;
            };
            self.ctrlHelper.error = function (data, status, headers, config) {
                self.unsetAccount();
            };
            apiService.Accounts.userdata({}, self.ctrlHelper);
        };

        return self;

    }]);
