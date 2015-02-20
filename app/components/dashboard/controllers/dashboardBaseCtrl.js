'use strict';

/**
 * Base controller for the Dashboard view.
 */
angular
    .module('Dashboard')
    .controller('dashboardBaseCtrl', ['$scope', function ($scope) {

        console.log("dashboardBaseCtrl");

        $scope.requests = [
            {"name": "John Q Public", "message": "I want to connect"},
            {"name": "Susie Q Public", "message": "I want to connect"},
            {"name": "Jennifer Doe", "message": "I want to connect"},
            {"name": "Jason Doe", "message": "I want to connect"},
        ];

        $scope.notifications = [
            {"name": "sri", "message": "Updated his profile"},
            {"name": "jason", "message": "Endorsed you"},
            {"name": "jane", "message": "gave you a 5-star rating for your recent service"},
            {"name": "jennifer", "message": "paid you for services rendered"},
        ];

    }]);