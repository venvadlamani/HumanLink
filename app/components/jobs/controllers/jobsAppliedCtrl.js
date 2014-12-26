'use strict';

/**
 * Jobs Applied (caregiver) controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsAppliedCtrl', ['$scope', 'apiService', 'userSession', '$window',
    function ($scope, apiService, userSession, $window) {
        /**
         * Populates $scope with jobs the caregiver has applied for.
         *
         * @returns void
         */
        var appliedJobsHelper = new HL.CtrlHelper();
        function getAppliedJobs() {
            appliedJobsHelper.success = function (data, status, headers, config) {
                $scope.appliedJobs = data.items;
            };
            apiService.Jobs.applied({}, appliedJobsHelper);
        };
        getAppliedJobs();

        $scope.getHours = function(startDate, endDate){
            var tmpStartDate = new Date(startDate);
            var tmpEndDate = new Date(endDate);
            $scope.hours = (tmpEndDate - tmpStartDate)/3600000;
        };

        /**
         * Release/cancel the job
         *
         * @returns void
         */
        $scope.releaseJob = function(jobID) {

            var releaseModel = {
                "job_id": parseInt(jobID)
            };

            alert("Cancel application functionality not built yet");
            /*
            console.log("cancelOBJ " + releaseModel);
            var releaseJobHelper = new HL.CtrlHelper();
            releaseJobHelper.success = function (data, status, headers, config) {
                $window.location.reload();
            };
            apiService.Jobs.cancel(releaseModel, releaseJobHelper);
            */
        };

    }]);
