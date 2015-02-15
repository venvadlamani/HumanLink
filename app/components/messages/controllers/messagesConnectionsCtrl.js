'use strict';

/**
 * Connections controller for the Messages view.
 */
angular
    .module('Messages')
    .controller('messagesConnectionsCtrl', ['$scope', function ($scope) {

        $scope.requests = [
            {"name": "John Q Public", "message": "I want to connect"},
            {"name": "Susie Q Public", "message": "I want to connect"},
            {"name": "Jennifer Doe", "message": "I want to connect"},
            {"name": "Jason Doe", "message": "I want to connect"},
        ];

    }]);
