angular.module('Accounts')

    .controller('profileController', ['$scope', 'apiService', function ($scope, apiService) {
        // TODO: obtain profile id from user session
        $scope.profile_id = '5275456790069248';

        apiService.getProfileInfo($scope.profile_id, function (resp) {
            $scope.profile = resp;
            // Don't forget to apply to update the template
            $scope.$apply();
        });

    }]);
