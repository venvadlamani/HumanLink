'use strict';

/**
 *  Controller for the contact view.
 */
angular
    .module('Home')
    .controller('contactCtrl', ['$scope', '$http',
        function ($scope, $http) {

            $scope.contactData = {};
            $scope.showContactForm = true;

            $scope.contact = function (model) {
                console.log(model);

                if (!model.message || !model.name || !model.email) {
                    return;
                }
                $http.post('/contact', model)
                    .success(function (data, status) {
                        $scope.siteAlert.type = "success";
                        $scope.siteAlert.message = "Success.";
                        $scope.showContactForm = false;
                    })
                    .error(function () {
                        $scope.siteAlert.type = "danger";
                        $scope.siteAlert.message = "Oops. Your message didn't go through. Please try again.";
                    });

            };

        }]);
