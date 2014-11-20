'use strict';

/**
 * Keeps track of the current logged in user.
 */
angular
    .module('Common')
    .factory('userSession', [function () {

        var self = this;
        self.account = null;

        self.setAccount = function(account) {
            self.account = account;
        };

        self.unsetAccount = function() {
            self.account = null;
        };

        self.isAuthorized = function() {
            return self.account !== null;
        };

        self.update = function() {
            // Get profile metadata and then call setAccount.
        };

        return self;

    }]);
