'use strict';

/**
 * Upcoming Jobs (Care-seekers) controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsUpcomingCtrl', ['$scope', 'apiService', 'userSession', '$state', '$window',
    function ($scope, apiService, userSession, $state, $window) {

        // Possible ng-switch values.
        var viewModes = ['upcoming_job', 'cancel_job_success'];
        $scope.viewMode = viewModes[0];

       //$scope.upcomingSearchFilter = 'Open'; DELETE
        /**
         * Populates $scope with jobs posted by the care-seeker.
         *
         * @returns void
         */
        var postedJobsHelper = new HL.CtrlHelper();
        function getPostedJobs() {
            postedJobsHelper.success = function (data, status, headers, config) {
                var tmpPostedJobs = data.items;
                if (tmpPostedJobs) {
                    $scope.postedJobs = tmpPostedJobs.filter(isJobStatusAccepted);
                };
                function isJobStatusAccepted(element) {
                    if (element.status === 'Accepted') {
                        return true;
                    } else {
                        return false;
                    };
                };
            };
            apiService.Jobs.posted({}, postedJobsHelper);
        };
        getPostedJobs();

        /**
         * cancel job.
         *
         * @returns void
         */
        $scope.cancelJob = function(jobID) {
            var cancelObj = {
                "job_id" : parseInt(jobID)
            };
            console.log("cancelOBJ " + cancelObj);
            var cancelJobHelper = new HL.CtrlHelper();
            cancelJobHelper.success = function (data, status, headers, config) {
                $scope.viewMode = viewModes[1];
                $window.location.reload();

            };
            apiService.Jobs.cancel(cancelObj, cancelJobHelper);
        };

    }]);
