'use strict';

angular
    .module('Accounts')
    .controller('settingsProfileCtrl',
    ['$scope', '$window', '$http', 'Constants', 'userSession',
        function ($scope, $window, $http, Constants, userSession) {

            var userdata = userSession.userdata;
            $scope.usr = userSession;
            var account_email = $scope.usr.userdata.email;

            // Placeholder until initial data is loaded.
            $scope.account = userdata;
            $scope.accountForm = angular.copy($scope.account);

            $scope.update = function (model) {
                if (!validate(model)) {
                    return;
                }
                $http.post('/post_account_basic', model)
                    .success(function (data, status) {
                        fetch(data, status);
                        $scope.siteAlert.type = "success";
                        $scope.siteAlert.message = "Your basic settings were updated successfully.";
                    })
                    .error(function () {
                        $scope.siteAlert.type = "danger";
                        $scope.siteAlert.message = "Oops. There was a problem. Please try again.";
                    });
            };

            var fetch = function (data, status) {
                // Full-refresh on name change since it is on the navbar.
                if (userdata.first != data.first ||
                    userdata.last != data.last) {
                    $window.location.reload();
                }
                $scope.account = data;
                $scope.accountForm = angular.copy(data);
            };

            var validate = function (model) {
                if (model.phone_number) {
                    if (!HL.helpers.isValidPhone(model.phone_number)) {
                        return false;
                    }
                    // Endpoint expects an integer.
                    model.phone_number = model.phone_number.replace(/\D/g, '');
                }
                return true;
            };

            var init = function () {
                $http.get('/get_account_basic?email=' + account_email)
                    .then(function (response) {
                        $scope.accountForm = response.data;
                    }, function (response) {
                        $scope.siteAlert.type = "danger";
                        $scope.siteAlert.message = ("Oops. " + response.status + " Error. Please try again.");
                    });
            };
            init();
        }]);
