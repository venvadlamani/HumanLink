'use strict';

/**
 * Nearby (primarily for caregiver) Jobs controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsNearbyCtrl', ['$scope', 'apiService', 'userSession', '$state', '$window',
    function ($scope, apiService, userSession, $state, $window) {

        // Possible ng-switch values.
        var viewModes = ['job_nearby_form', 'job_apply_success', 'job_apply_error'];
        $scope.viewMode = viewModes[0];

        /**
         * Populates $scope with jobs nearby the caregiver.
         *
         * @returns void
         */
        var nearbyJobsHelper = new HL.CtrlHelper();
        function getNearbyJobs() {
            nearbyJobsHelper.success = function (data, status, headers, config) {
                $scope.nearbyJobs = data.items;
            };
            apiService.Jobs.nearby({}, nearbyJobsHelper);
        };
        getNearbyJobs();

        $scope.getHours = function(startDate, endDate){
            var tmpStartDate = new Date(startDate);
            var tmpEndDate = new Date(endDate);
            $scope.hours = (tmpEndDate - tmpStartDate)/3600000;
        };

        /**
         * Apply for job.
         *
         * @returns void
         */
        $scope.applyJob = function(jobID) {

            var applyModel = {
                "job_id": parseInt(jobID)
            };

            var applyJobHelper = new HL.CtrlHelper();
            applyJobHelper.success = function (data, status, headers, config) {
                $scope.applyJobs = data.items;
                $scope.viewMode = viewModes[1];
                $window.location.reload();
            };
            applyJobHelper.error = function (data, status, headers, config) {
                $scope.applyJobs = data.items;
                $scope.viewMode = viewModes[2];
            };
            apiService.Jobs.apply(applyModel, applyJobHelper);
        };

    }]);
