'use strict';

/**
 * Controller for the login view.
 */
angular
    .module('Accounts')
    .controller('loginCtrl', ['$scope', '$window', '$location', 'apiService',
                'userSession',
     function ($scope, $window, $location, apiService, userSession) {

        // Reference to the base ctrlHelper.
        var ctrlHelper = $scope.$parent.ctrlHelper;
        ctrlHelper.reset();

        if (userSession.isAuthorized()) {
            $location.path('/edit');
        }

        $scope.loginModel = {
            email: '',
            password: ''
        };

        $scope.login = function (model) {
            ctrlHelper.success = function (data, status, headers, config) {
                // Redirect to profile page.
                $window.location.href = HL.baseUrl + '/accounts#/edit';
            };
            apiService.Accounts.login(model, ctrlHelper);
        };

    }]);
