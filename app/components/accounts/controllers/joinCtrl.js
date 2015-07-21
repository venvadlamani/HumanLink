'use strict';

/**
 * Controller for the signup view.
 */
angular
    .module('Accounts')
    .controller('joinCtrl', ['$scope', '$window', 'apiService', 'userSession', '$location',
        function($scope, $window, apiService, userSession, $location) {

            // Reference to the base ctrlHelper.
            var ctrlHelper = $scope.$parent.ctrlHelper;
            ctrlHelper.reset();

            if (userSession.isAuthorized()) {
                $location.path('/profile');
            }

            // Possible ng-switch values.
            var viewModes = ['join_form', 'join_success'];
            var defaultModel = {
                email: '',
                password: '',
                password_confirm: '',
                account_type: 0
            };

            $scope.viewMode = viewModes[0];
            $scope.signupModel = defaultModel;

            $scope.join = function(model) {
                ctrlHelper.reset();
                if (!validate(model, ctrlHelper)) {
                    return;
                }
                ctrlHelper.success = function(data, status, headers, config) {
                    $scope.viewMode = viewModes[1];
                };
                apiService.Accounts.signup(model, ctrlHelper);
            };

            $scope.cancel = function() {
                $scope.signupModel = defaultModel;
                $scope.$parent.previous();
            };

            var validate = function(model, ctrlHelper) {
                var errors = [];
                if (!model.email || !model.password || !model.password_confirm) {
                    errors.push('All fields are required.');
                }
                if (model.password !== model.password_confirm) {
                    errors.push('Password does not match the confirmation.');
                }
                if (errors.length) {
                    ctrlHelper.isLoading = false;
                    ctrlHelper.isValid = false;
                    ctrlHelper.errors = errors;
                    return false;
                }
                return true;
            };

        }
    ]);