'use strict';

/**
 * Base controller for the home module.
 */
angular
    .module('Admin')
    .controller('inviteCtrl', ['$scope', '$http', 'userSession',
        function ($scope, $http, userSession) {

            $scope.inviteEmail = function (model) {
                console.log(model);
                $http.post('/post_admin_invite', model)
                    .success(function (data, status) {
                        $scope.siteAlert.type = "success";
                        $scope.siteAlert.message = "Your email was sent successfully.";
                    })
                    .error(function () {
                        $scope.siteAlert.type = "danger";
                        $scope.siteAlert.message = "Oops. There was a problem. Please try again.";
                    });

            };

        }]);
