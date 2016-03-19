'use strict';

/**
 * Press controller
 */
angular
    .module('Accounts')
    .controller('connectionsCtrl', ['$scope', 'userSession', '$http',
        function ($scope, userSession, $http) {

            $scope.connections = {};
            $scope.usr = userSession;
            var account_id = $scope.usr.userdata.account_id;

            var init = function () {
                $http({
                    url: '/get_connections',
                    method: "GET",
                    params: {account_id: account_id}
                }).then(function (response) {
                    $scope.connections = response.data;
                }, function (response) {
                    $scope.siteAlert.type = "danger";
                    $scope.siteAlert.message = ("Oops. " + response.status + " Error. Please try again.");
                });
            };
            init();

        }]);
