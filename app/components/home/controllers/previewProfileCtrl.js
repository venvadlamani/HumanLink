'use strict';

/**
 * Press controller
 */
angular
    .module('Home')
    .controller('previewProfileCtrl', ['$scope', '$window', '$stateParams', '$http',
        function ($scope, $window, $stateParams, $http) {

            var caregiverKey = $stateParams.caregiver_key;
            $scope.profile = {};

            var init = function () {
                $http.get('caregiver_profile?account_id=' + caregiverKey)
                    .then(function (response) {
                        $scope.profile = response.data;
                    });
            };
            init();

        }]);
