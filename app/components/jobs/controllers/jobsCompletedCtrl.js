'use strict';

/**
 * Completed Jobs (caregiver) controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsCompletedCtrl', ['$scope', 'apiService', 'userSession',
    function ($scope, apiService, userSession) {

        /**
         * Populates $scope with jobs that the caregiver was selected for and completed.
         *
         * @returns void
         */
        var completedJobsHelper = new HL.CtrlHelper();
        function getCompletedJobs() {
            completedJobsHelper.success = function (data, status, headers, config) {
                $scope.completedJobs = data.items;
            };
            apiService.Jobs.selected({}, completedJobsHelper);
        };
        getCompletedJobs();

        $scope.getHours = function(startDate, endDate){
            var tmpStartDate = new Date(startDate);
            var tmpEndDate = new Date(endDate);
            $scope.hours = (tmpEndDate - tmpStartDate)/3600000;
        };

    }]);
