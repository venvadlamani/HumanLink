'use strict';

/**
 * Base controller for the Connections module.
 */
angular
    .module('Connections')
    .controller('connectionsBaseCtrl', ['$scope', '$filter', 'apiService', 'userSession',
        function ($scope, $filter, apiService, userSession) {

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

            function getFavoritesInfo() {
                $scope.favorites = {};
                if ($scope.connections) {
                    for (i = 0; i < $scope.connections.length; i++) {
                        if ($scope.connections.is_favorite) {
                            $scope.favorites.push($scope.connections[i]);
                        }
                    }
                }
            };
            getFavoritesInfo();

            $scope.messageConnection = function (accountID) {
                console.log("message connection " + accountID);
            };

            $scope.removeConnection = function (accountID) {
                var payload = {
                    "account_id": accountID
                };
                var removeConnectionsHelper = new HL.CtrlHelper();
                removeConnectionsHelper.success = function (payload, status, headers, config) {
                    $scope.connections = $filter('filter')($scope.connections, {account_id: !accountID});
                };
                apiService.Connections.remove(payload, removeConnectionsHelper);
            };

            $scope.sendConnectionRequest = function (accountID) {
                var payload = {
                    "account_id": accountID
                };
                var requestConnectionsHelper = new HL.CtrlHelper();
                requestConnectionsHelper.success = function (payload, status, headers, config) {
                };
                apiService.Connections.request(payload, requestConnectionsHelper);
            };

            $scope.detailsConnection = function (accountID) {
                console.log(" connection details " + accountID);
            };

        }]);
