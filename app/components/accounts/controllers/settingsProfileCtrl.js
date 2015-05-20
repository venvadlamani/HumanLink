'use strict';

angular
    .module('Accounts')
    .controller('settingsProfileCtrl',
    ['$scope', '$window', 'Constants', 'userSession', 'apiService',
    function ($scope, $window, Constants, userSession, apiService) {

        var userdata = userSession.userdata;
        var templBase = '/views/accounts/partials/settings/';
        var updateReq = new HL.CtrlHelper();

        // Placeholder until initial data is loaded.
        $scope.account = userdata;
        $scope.accountForm = angular.copy($scope.account);

        $scope.secondaryTemplate = {
            "Caregiver": templBase + 'profile_caregiver.html',
            "Careseeker": templBase + 'profile_careseeker.html'
        };

        $scope.accountTypes = Constants.accountTypes;

        $scope.update = function (model) {
            if (!validate(model)) {
                return;
            }
            updateReq.success = function (data, status) {
                fetch(data, status);
                $scope.siteAlert.type = "success";
                $scope.siteAlert.message = "Changes have been saved.";
            };
            updateReq.failure = function (data, status) {
                $scope.siteAlert.type = "danger";
                $scope.siteAlert.message = "Uh-oh, there was a problem.";
            };
            apiService.Accounts.update(model, updateReq);
        };

        var fetch = function (data, status) {
            // Full-refresh on name change since it is on the navbar.
            if (userdata.first != data.first ||
                userdata.last != data.last) {
                $window.location.reload();
            }
            $scope.account = data;
            $scope.accountForm = angular.copy(data);
        };

        var validate = function (model) {
            if (model.phone_number) {
                if (!HL.helpers.isValidPhone(model.phone_number)) {
                    return false;
                }
                // Endpoint expects an integer.
                model.phone_number = model.phone_number.replace(/\D/g,'');
            }
            return true;
        };

        var init = function() {
            updateReq.success = function (data, status) {
                fetch(data, status);
            };
            apiService.Accounts.get(userdata.account_id, updateReq);
        };
        init();
    }]);
