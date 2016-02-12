'use strict';

/**
 * Controller for caregiver profile PREVIEW page
 */
angular
    .module('Accounts')
    .controller('manageProfileCtrl', ['$scope', 'apiService', 'userSession',
        function ($scope, apiService, userSession) {

            var userdata = userSession.userdata;
            var CaregiverReq = new HL.CtrlHelper();
            var updateReq = new HL.CtrlHelper();

            $scope.profile = {};

            init();
            function init() {
                updateReq.success = function (accountData, status) {
                    angular.extend($scope.profile, accountData);
                };
                apiService.Accounts.get(userdata.account_id, updateReq);

                CaregiverReq.success = function (caregiverData, status) {
                    angular.extend($scope.profile, caregiverData);
                };
                apiService.Accounts.caregiver.get(userdata.account_id, CaregiverReq);
            }

        }]);
