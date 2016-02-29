'use strict';

/**
 * General Caregiver controller
 */
angular
    .module('Home')
    .controller('caregiverGeneralCtrl', ['$scope', '$http', function ($scope, $http) {


        $scope.showCaregiverForm = true;
        $scope.caregiverGeneralUpdate = caregiverGeneralUpdate;

        function caregiverGeneralUpdate(model) {

            if (!model.name || !model.phone || !model.location) {
                return;
            }

            $http.post('/submit_caregiver_general', model)
                .success(function (data, status) {
                    $scope.siteAlert.type = "success";
                    $scope.siteAlert.message = "Changes have been saved.";
                    $scope.showCaregiverForm = false;
                })
                .error(function () {
                    // Dang.
                });
        }


    }]);
