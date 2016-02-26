'use strict';

/**
 * Controller for the password reset
 */
angular
    .module('Accounts')
    .controller('resetCtrl', ['$scope', '$http', function ($scope, $http) {

        var viewModes = ['reset_form', 'reset_sent'];
        $scope.viewMode = viewModes[0];

        $scope.resetModel = {
            email: ''
        };

        $scope.reset = function (model) {
            $http.post('/reset', model)
                .success(function (data, status) {
                    $scope.viewMode = viewModes[1];
                })
                .error(function () {
                    $scope.siteAlert.type = "danger";
                    $scope.siteAlert.message = "Oops. There was a problem. Please try again.";
                });
        };

    }]);
