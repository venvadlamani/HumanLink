'use strict';

/**
 * Pending controller (for care-seekers) for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsPendingCtrl', ['$scope', 'apiService', 'userSession', '$stateParams',
    function ($scope, apiService, userSession, $stateParams) {
        /**
         * Populates $scope with jobs posted by care-seeker and wih status open.
         *
         * @returns void
         */
        var pendingJobsHelper = new HL.CtrlHelper();
        function getPendingJobs() {
            pendingJobsHelper.success = function (data, status, headers, config) {
                var tmpPendingJobs = data.items;
                function isJobStatusAccepted(element) {
                    if (element.status === 'Open'){
                        return true;
                    } else{
                        return false;
                    };
                };
                if(tmpPendingJobs){
                    $scope.pendingJobs = tmpPendingJobs.filter(isJobStatusAccepted);
                }
            };
            apiService.Jobs.posted({}, pendingJobsHelper);
        };
        getPendingJobs();

        $scope.viewResponses = function (jobID) {

        };
    }]);
