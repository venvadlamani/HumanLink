'use strict';

/**
 * Press controller
 */
angular
    .module('Home')
    .controller('previewSeekerProfileCtrl', ['$scope', '$window', '$stateParams', '$http',
        function ($scope, $window, $stateParams, $http) {

            var account_id = $stateParams.account_id;
            $scope.aboutMe = {};

            var init = function () {
                $http.get('/seeker_profile?account_id=' + account_id)
                    .then(function (response) {
                        $scope.aboutMe = response.data;
                    });
            };
            init();

        }]);
