'use strict';

/**
 * Previous Jobs (Care-seekers) controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsPreviousCtrl', ['$scope', 'apiService', 'userSession', '$state',
    function ($scope, apiService, userSession, $state) {
        $scope.upcomingSearchFilter = 'Open';

        /**
         * Populates $scope with jobs posted by the care-seeker.
         *
         * @returns void
         */
        var postedJobsHelper = new HL.CtrlHelper();
        function getPostedJobs() {
            postedJobsHelper.success = function (data, status, headers, config) {
                var tmpPostedJobs = data.items;
                var tmpDate = new Date();
                if (tmpPostedJobs) {
                    $scope.postedJobs = tmpPostedJobs.filter(isJobPrevious);
                };
                function isJobPrevious(element) {
                    if (element.end_date < tmpDate) {
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
                $state.go('upcoming');
            };
            apiService.Jobs.cancel(cancelObj, cancelJobHelper);
        };

    }]);
