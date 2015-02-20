'use strict';

/**
 * Inbox controller for the Messages view.
 */
angular
    .module('Messages')
    .controller('messagesInboxCtrl', ['$scope', function ($scope) {

        $scope.inboxModel = [
            {
                "name":"kashi",
                "date":"Tue",
                "messageID":"1234",
                "lastMessage": "this is really great. so good to hear."
            },
            {
                "name":"susie q.",
                "date":"Feb 6",
                "messageID":"3456",
                "lastMessage": "this is really great. so good to hear."
            },
            {
                "name":"susie q.",
                "date":"Feb 6",
                "messageID":"3456",
                "lastMessage": "this is really great. so good to hear."
            },
            {
                "name":"susie q.",
                "date":"Feb 6",
                "messageID":"3456",
                "lastMessage": "this is really great. so good to hear."
            },
            {
                "name":"sri",
                "date":"Feb 6",
                "messageID":"6556",
                "lastMessage": "this is really great. so good to hear."
            },

        ];

    }]);
