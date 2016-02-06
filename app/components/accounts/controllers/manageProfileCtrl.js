'use strict';

/**
 * Controller for account management page
 */
angular
    .module('Accounts')
    .controller('manageProfileCtrl', ['$scope', 'apiService', 'userSession',
        function ($scope, apiService, userSession) {

            var userdata = userSession.userdata;
            var CaregiverReq = new HL.CtrlHelper();
            var updateReq = new HL.CtrlHelper();

            $scope.caregiverProfile = {};
            $scope.caregiverAccount = {};

            //DUMMY DATA - TO BE REMOVED
            $scope.profile = {
                city: 'Fayetteville',
                state: 'AR',
                mobile_redacted: '(xxx) xxx - xx23',

                education: [{
                    title: 'CNA',
                    completion: 'NTI - Completed, December 2014'
                }, {
                    title: 'LPN',
                    completion: 'NTI 2014 - current'
                }],
            };

            var fetchCaregiver = function (data, success) {
                $scope.caregiverProfile = data;
                $scope.caregiverForm = angular.copy(data);
                $scope.caregiverDetails = angular.copy(data);
            };

            init();
            function init() {

                updateReq.success = function (accountData, status) {
                    angular.extend($scope.profile, accountData);
                    $scope.profile.pictureUrl = 'profile_' + accountData.first +
                        accountData.last + '.png';
                    $scope.profile.bannerUrl = 'banner_' + accountData.first +
                        accountData.last + '.png';
                };
                apiService.Accounts.get(userdata.account_id, updateReq);

                CaregiverReq.success = function (caregiverData, status) {
                    angular.extend($scope.profile, caregiverData);
                };
                apiService.Accounts.caregiver.get(userdata.account_id, CaregiverReq);

            }

        }]);
