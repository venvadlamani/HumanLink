'use strict';

/**
 *  Controller for the contact view.
 */
angular
    .module('Accounts')
    .controller('contactCtrl', ['$scope', 'apiService', 'userSession',
        function ($scope, apiService, userSession) {

            var userData = userSession.userdata;
            var updateReq = new HL.CtrlHelper();

            $scope.contactData = userData;

            $scope.contact = function (model) {
                if (!model.message) {
                    return;
                }
                updateReq.success = function (data, status) {
                    $scope.siteAlert.type = "success";
                    $scope.siteAlert.message = "Message has been sent. You will hear from someone soon. Thank you.";
                };
                updateReq.failure = function (data, status) {
                    $scope.siteAlert.type = "danger";
                    $scope.siteAlert.message = "Uh-oh, there was a problem.";
                };

                apiService.Accounts.contact(model, updateReq);
            };

        }]);
