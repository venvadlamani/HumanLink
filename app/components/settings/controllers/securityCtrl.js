'use strict';

/**
 * Security controller
 */
angular
    .module('Settings')
    .controller('securityCtrl', ['$scope', '$window', function ($scope, $window) {

        var updateReq = new HL.CtrlHelper();

        var validate = function (model) {
            if (!model.password || !model.password_confirm) {
                $scope.siteAlert.type = "danger";
                $scope.siteAlert.message = "All fields are required.";
            }
            if (model.password !== model.password_confirm) {
                $scope.siteAlert.type = "danger";
                $scope.siteAlert.message = "Password does not match the confirmation.";
            }
            return true;
        };

        $scope.update = function (model) {
            if (!validate(model)) {
                return false;
            }
        };


    }]);
