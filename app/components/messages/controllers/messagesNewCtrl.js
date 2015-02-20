'use strict';

/**
 * Base controller for the Messages view.
 */
angular
    .module('Messages')
    .controller('messagesNewCtrl', ['$scope', 'apiService', 'userSession', '$stateParams',
    function ($scope, apiService, userSession, $stateParams) {

        $scope.account_id = $stateParams.account_id;

        var viewModes = ['message_form', 'message_success'];
        $scope.viewMode = viewModes[0];


        $scope.sendtolist = [
            {
                'accountID' : 4785074604081152,
                'first' : "Peter"
            },
            {
                'accountID' : 5689697795833856,
                'first' : "Kanat"
            },
            {
                'accountID' : 5629499534213120,
                'first' : "Ariana"
            },
            {
                'accountID' : 5971172772544512,
                'first' : "Justin"
            },
            {
                'accountID' : 6252647749255168,
                'first' : "Ven"
            },
            {
                'accountID' : 6710044586409984,
                'first' : "Jackie"
            }
        ];
        /**
         * get connection(s).
         *
         * @returns void
         */
        var connectionsObj ={};
        var connectionsHelper = new HL.CtrlHelper();
        connectionsHelper.success = function (connectionsObj, status, headers, config) {
        };
        apiService.Connections.my(connectionsObj, connectionsHelper);


        /**
         * sends message to the connection(s).
         *
         * @returns void
         */
        $scope.sendMessage = function(message){
            var messageObj ={};
            messageObj.recipients = [message.sender.accountID]; //array of recipients
            messageObj.subject = message.subject;
            messageObj.text = message.text;
            var messageHelper = new HL.CtrlHelper();
            messageHelper.success = function (messageObj, status, headers, config) {
                $scope.viewMode = viewModes[1];
            };
            apiService.Messages.new(messageObj, messageHelper);
        };

    }]);
