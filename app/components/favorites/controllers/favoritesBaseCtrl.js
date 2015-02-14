'use strict';

/**
 * Base controller for the Collections module.
 */
angular
    .module('Favorites')
    .controller('favoritesBaseCtrl', ['$scope', 'apiService', 'userSession',
    function ($scope, apiService, userSession) {

        /**
         * Obtains all favorites.
         *
         * @returns void
         */
        var connectionsHelper = new HL.CtrlHelper();
        function getConnectionsInfo() {
            connectionsHelper.success = function (data, status, headers, config) {
                $scope.connections = data.items;
            };
        apiService.Connections.my({}, connectionsHelper);
        }
        getConnectionsInfo();

    }]);

