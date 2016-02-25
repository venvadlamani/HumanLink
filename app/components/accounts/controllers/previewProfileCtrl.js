'use strict';

/**
 * Press controller
 */
angular
    .module('Accounts')
    .controller('previewProfileCtrl', ['$scope', 'userSession', '$http',
        function ($scope, userSession, $http) {

            $scope.profile = {};
            $scope.usr = userSession;
            var account_id = $scope.usr.userdata.account_id;
            var email = $scope.usr.userdata.email;

            var init = function () {
                $http({
                    url: '/get_caregiver_profile_preview',
                    method: "GET",
                    params: {account_id: account_id, email: email}
                }).then(function (response) {
                    $scope.profile = angular.extend(response.data.caregiver, response.data.account, $scope.usr.userdata);
                }, function (response) {
                    $scope.siteAlert.type = "danger";
                    $scope.siteAlert.message = ("Oops. " + response.status + " Error. Please try again.");
                });
            };
            init();

        }]);
