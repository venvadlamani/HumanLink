'use strict';

/**
 * Base controller for the Connections module.
 */
angular
    .module('Connections')
    .controller('connectionsBaseCtrl', ['$scope', 'apiService', 'userSession',
    function ($scope, apiService, userSession) {

        /**
         * Populates $scope with connections.
         *
         * @returns void
         */
        var connectionsHelper = new HL.CtrlHelper();
        function getConnectionsInfo() {
            connectionsHelper.success = function (data, status, headers, config) {
                $scope.connections = data.items;
            };
            apiService.Connections.my({}, connectionsHelper);
        };
        getConnectionsInfo();

    }]);
