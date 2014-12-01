'use strict';

/**
 * Base controller for the Connections module.
 */
angular
    .module('Connections')
    .controller('connectionsBaseCtrl', ['$scope', function ($scope) {

        /**
         * Populates $scope with connections.
         *
         * @returns void
         */
        $scope.getConnections = function () {
            console.log('getConnections');
        };
    }]);
