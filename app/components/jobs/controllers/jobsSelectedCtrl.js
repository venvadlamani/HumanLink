'use strict';

/**
 * Selected (upcoming) Jobs for caregivers controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsSelectedCtrl', ['$scope', 'apiService', 'userSession', '$window',
    function ($scope, apiService, userSession, $window) {

        // Possible ng-switch values.
        var viewModes = ['upcoming_job', 'cancel_job_success'];
        $scope.viewMode = viewModes[0];

        /**
         * Populates $scope with jobs that the caregiver was selected for
         *
         * @returns void
         */
        var selectedJobsHelper = new HL.CtrlHelper();
        function getSelectedJobs() {
            selectedJobsHelper.success = function (data, status, headers, config) {
                $scope.selectedJobs = data.items;
            };
            apiService.Jobs.selected({}, selectedJobsHelper);
        };
        getSelectedJobs();

        $scope.getHours = function(startDate, endDate){
            var tmpStartDate = new Date(startDate);
            var tmpEndDate = new Date(endDate);
            $scope.hours = (tmpEndDate - tmpStartDate)/3600000;
        };

        $scope.cancelJob= function(jobID){
            var cancelObj = {
                "job_id" : parseInt(jobID)
            };
            var cancelJobHelper = new HL.CtrlHelper();
            cancelJobHelper.success = function (data, status, headers, config) {
                $scope.viewMode = viewModes[1];
                $window.location.reload();

            };
            apiService.Jobs.cancel(cancelObj, cancelJobHelper);
        };
    }]);
