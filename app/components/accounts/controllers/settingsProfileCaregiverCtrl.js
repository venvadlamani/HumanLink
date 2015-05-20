'use strict';

angular
    .module('Accounts')
    .controller('settingsProfileCaregiverCtrl', ['$scope', 'Constants', 'apiService',
    function ($scope, Constants, apiService) {
        var updateReq = new HL.CtrlHelper();

        $scope.showLicenseForm = false;
        $scope.showCertificationForm = false;
        $scope.showExpertiseForm = false;
        $scope.showLanguageForm = false;

        $scope.allergies = Constants.allergies;
        $scope.careServices = Constants.careServices;
        $scope.expertise = Constants.expertise;
        $scope.languages = Constants.languages;
        $scope.transportation = Constants.transportation;
        $scope.states = Constants.states;

        $scope.caregiver = null;
        $scope.caregiverForm = null;
        $scope.caregiverDetails = null;

        $scope.caregiverUpdate = function (model) {
            if (!validate(model)) {
                return;
            }
            // Maybe nothing has been changed.
            if (angular.equals($scope.caregiver, model)) {
                return;
            }
            if (model.year) {
                model.dob = new Date(model.year, 0);
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
            apiService.Accounts.caregiver.update(model, updateReq);
        };

        var fetch = function (data, success) {
            if (data.dob) {
                data.year = new Date(data.dob).getFullYear();
            }
            $scope.caregiver = data;
            $scope.caregiverForm = angular.copy(data);
            $scope.caregiverDetails = angular.copy(data);
        };

        var validate = function (model) {
            if (model.year && (model.year < 1900 ||
                model.year > new Date().getFullYear() - 10)) {
                return false;
            }
            return true;
        };

        var init = function (accountId) {
            updateReq.success = function (data, status) {
                fetch(data, status);
            };
            apiService.Accounts.caregiver.get(accountId, updateReq);
        };
        init($scope.account.account_id);
    }]);