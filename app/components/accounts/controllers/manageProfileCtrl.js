'use strict';

/**
 * Controller for account management page
 */
angular
    .module('Accounts')
    .controller('manageProfileCtrl', ['$scope', 'apiService', 'userSession',
                function ($scope, apiService, userSession) {
        var profileHelper = new HL.CtrlHelper(),
            patientsHelper = new HL.CtrlHelper();

        $scope.profile = {
            money_saved: 150,
        };

        getInfo();

        function getInfo () {
            profileHelper.success = function (data, status, headers, config) {
                angular.extend($scope.profile, data);
                $scope.profile.pictureUrl = 'profile_' + data.first +
                    data.last + '.png';
                $scope.profile.bannerUrl = 'banner_' + data.first +
                    data.last + '.png';
            };

            patientsHelper.success = function (data, status, headers, config) {
                $scope.careRecipients = data;
            };

            apiService.Accounts.get(userSession.userdata.account_id,
                                    profileHelper);
            apiService.Accounts.patients.list(patientsHelper);
        }

        /**
         * Add's care_recipient under current account.
         *
         * @return void
         */
        $scope.addCareRecipient = function () {
            console.log('addCareRecipient');
        };
    }]);
