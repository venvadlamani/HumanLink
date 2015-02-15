'use strict';

/**
 * Notifications controller for the Messages view.
 */
angular
    .module('Messages')
    .controller('messagesNotificationsCtrl', ['$scope', function ($scope) {

        $scope.notifications = [
            {"name": "sri", "message": "Updated his profile"},
            {"name": "jason", "message": "Endorsed you"},
            {"name": "jane", "message": "gave you a 5-star rating for your recent service"},
            {"name": "jennifer", "message": "paid you for services rendered"},
        ];

    }]);
