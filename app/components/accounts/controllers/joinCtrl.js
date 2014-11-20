'use strict';

/**
 * Controller for the signup view.
 */
angular
    .module('Accounts')
    .controller('joinCtrl', ['$scope', '$window', 'apiService',
    function ($scope, $window, apiService) {

        // Reference to the base ctrlHelper.
        var ctrlHelper = $scope.$parent.ctrlHelper;
        ctrlHelper.reset();

        // Possible ng-switch values.
        var viewModes = ['join_form', 'join_success'];

        $scope.viewMode = viewModes[0];
        $scope.signupModel = {
            email: '',
            password: '',
            password_confirm: ''
        };

        $scope.join = function(model) {
            ctrlHelper.success = function (data, status, headers, config) {
                $scope.viewMode = viewModes[1];
            };
            apiService.Accounts.signup(model, ctrlHelper);
        };

        $scope.cancel = function() {
            $scope.signupModel = {};
            $scope.$parent.previous();
        };

    }]);
