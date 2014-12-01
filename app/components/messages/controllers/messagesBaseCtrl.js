'use strict';

/**
 * Base controller for the Messages view.
 */
angular
    .module('Messages')
    .controller('messagesBaseCtrl', ['$scope', function ($scope) {

        /**
         * Takes form input and sends a message to a specified user.
         *
         * @return void
         */
        $scope.newMessage = function () {
            console.log('newMessage');
        };

        /**
         * Populates $scope with inbox messages.
         *
         * @return void
         */
        $scope.getMessages = function () {
            console.log('getMessages');
        };
    }]);
