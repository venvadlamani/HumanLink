'use strict';

/**
 * Controller for the login view.
 */
angular
    .module('Accounts')
    .controller('loginCtrl', ['$scope', '$window', 'apiService', 'userSession',
     function ($scope, $window, apiService, userSession) {

        // Reference to the base ctrlHelper.
        var ctrlHelper = $scope.$parent.ctrlHelper;
        ctrlHelper.reset();

        $scope.loginModel = {
            email: '',
            password: ''
        };

        $scope.login = function(model) {
            ctrlHelper.success = function (data, status, headers, config) {
                // Redirect to home page.
                $window.location.href = HL.baseUrl;
            };
            apiService.Accounts.login(model, ctrlHelper);
        };

    }]);
