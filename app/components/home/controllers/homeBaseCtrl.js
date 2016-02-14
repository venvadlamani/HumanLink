'use strict';

/**
 * Base controller for the home module.
 */
angular
    .module('Home')
    .controller('homeBaseCtrl', ['$scope', '$window', '$http',
        function ($scope, $window, $http) {

            $scope.searchCaregiverResults = {};
            var results = [];

            var init = function (model) {
                $http.get('get_caregiver_general/search.json')
                    .then(function (response) {
                        angular.forEach(response.data, function (val, key) {
                            results.push(key);
                        });
                        $scope.searchCaregiverResults = angular.extend(response.data);
                    });
            };
            init();

            /**
             * Go back to the previous page/view.
             * @return void
             */
            $scope.previous = function () {
                $window.history.back();
            };

            $scope.caregiverDetails = function (model) {
                console.log(model);
            };

        }]);
