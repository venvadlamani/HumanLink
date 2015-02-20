'use strict';

/**
 * Detail controller for the Messages .
 */
angular
    .module('Messages')
    .controller('messagesDetailCtrl', ['$scope', function ($scope) {

        $scope.messageDetails = [
            {
                "name" : "sri",
                "message" : "testing the waters",
                "datetime" : "2015-02-11T23:53:45.147Z"
            },
            {
                "name" : "me",
                "message" : "yeah? me too!",
                "datetime" : "2015-02-12T23:53:45.147Z"
            },
            {
                "name" : "sri",
                "message" : "water is cold",
                "datetime" : "2015-02-14T23:53:45.147Z"
            },
            {
                "name" : "me",
                "message" : "not here. water is warm and trending hotttt.",
                "datetime" : "2015-02-14T23:53:45.147Z"
            },
        ];

        $scope.sendMessage = function(message) {
            console.log(message);
            var timestamp = new Date();
            var newMessage = { "name" : "me", "message" : $scope.newMessage, "datetime": timestamp };
            console.log (newMessage);

            var newThread = $scope.messageDetails.push(newMessage);

        };

    }]);
