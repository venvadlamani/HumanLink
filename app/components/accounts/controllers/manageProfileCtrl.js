'use strict';

/**
 * Controller for account management page
 */
angular
    .module('Accounts')
    .controller('manageProfileCtrl', ['$scope', function ($scope) {
        $scope.profile = {
            name: 'First Last',
            phone: '(555)555-5555',
            money_saved: 150,
        };

        /**
         * Retrieves all care_recipients under account and assigns them into $scope.
         *
         * @return void
         */
        $scope.getCareRecipients = function () {
            $scope.care_recipients = [
                {name: 'Care Recipient Name', phone: '(555)555-5555'},
                {name: 'Care Recipient Name', phone: '(555)555-5555'},
                {name: 'Care Recipient Name', phone: '(555)555-5555'},
                {name: 'Care Recipient Name', phone: '(555)555-5555'}
            ];
        };

        /**
         * Add's care_recipient under current account.
         *
         * @return void
         */
        $scope.addCareRecipient = function () {
            console.log('addCareRecipient');
        };

        $scope.getCareRecipients();
    }]);
