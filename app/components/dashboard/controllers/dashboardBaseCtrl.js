'use strict';

/**
 * Base controller for the dashboard module.
 */
angular
    .module('Dashboard')
    .controller('dashboardBaseCtrl', ['$scope', '$window', function ($scope, $window) {

        /**
         * Go back to the previous page/view.
         * @return void
         */
        $scope.previous = function () {
            $window.history.back();
        };

    }]);
