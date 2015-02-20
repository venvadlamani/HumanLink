'use strict';

/**
 * Inbox controller for the Messages view.
 */
angular
    .module('Messages')
    .controller('messagesInboxCtrl', ['$scope', 'apiService', 'userSession',
    function ($scope, apiService, userSession) {

        /**
         * Populates $scope with messages.
         *
         * @returns void
         */
        var inboxHelper = new HL.CtrlHelper();
        function getMessages() {
            inboxHelper.success = function (data, status, headers, config) {
                $scope.messages = data.items;
            };
        apiService.Messages.inbox({}, inboxHelper);
        }
        getMessages();

    }]);
