'use strict';

/**
 * Pending connections controller for the Connections module.
 */
angular
    .module('Connections')
    .controller('connectionsPendingCtrl', ['$scope', 'apiService', 'userSession', '$window',
        function ($scope, apiService, userSession, $window) {
            /**
             * Populates $scope with pending requests.
             *
             * @returns void
             */
            var pendingConnectionsHelper = new HL.CtrlHelper();

            function geInfo() {
                pendingConnectionsHelper.success = function (data, status, headers, config) {
                    $scope.pendingConnections = data.items;
                };
                apiService.Connections.pending(data, pendingConnectionsHelper);
            }

            geInfo();

            $scope.accept = function (accountID) {
                var acceptObj = {
                    'account_id': accountID
                };
                var acceptConnectionsHelper = new HL.CtrlHelper();
                acceptConnectionsHelper.success = function (acceptObj, status, headers, config) {
                    $scope.connections = $filter('filter')($scope.connections, {account_id: accountID});
                };
                apiService.Connections.accept(acceptObj, acceptConnectionsHelper);
            };

            $scope.decline = function (accountID) {
                var payload = {
                    'account_id': accountID
                };
                var declineConnectionsHelper = new HL.CtrlHelper();
                declineConnectionsHelper.success = function (payload, status, headers, config) {
                    $window.location.reload();
                };
                apiService.Connections.decline(payload, declineConnectionsHelper);
            };

        }]);
