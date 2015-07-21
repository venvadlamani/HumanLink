'use strict';

/**
 * Controller for the login view.
 */
angular
    .module('Accounts')
    .controller('loginCtrl', ['$scope', '$window', '$location', 'apiService',
        'userSession', '$state',
        function($scope, $window, $location, apiService, userSession, $state) {

            // Reference to the base ctrlHelper.
            var ctrlHelper = $scope.$parent.ctrlHelper;
            ctrlHelper.reset();

            // Get initial accessed page
            $scope.redirectPage = '';
            var redirectUrl = $location.path().split('/');
            if (typeof redirectUrl[2] != 'undefined') {
                $scope.redirectPage = decodeURIComponent(redirectUrl[2]);
            }

            if (userSession.isAuthorized()) {
                $location.path('/profile');
            }

            $scope.loginModel = {
                email: '',
                password: ''
            };

            $scope.login = function(model) {
                ctrlHelper.reset();
                if (!model.email || !model.password) {
                    return;
                }


                ctrlHelper.success = function(data, status, headers, config) {

                    if ($scope.redirectPage == '') {
                        $window.location.href = HL.baseUrl + '/accounts';
                    } else {
                        $state.go($scope.redirectPage, {}, {
                            reload: true
                        });
                    }
                };
                apiService.Accounts.login(model, ctrlHelper);
            };

        }
    ]);