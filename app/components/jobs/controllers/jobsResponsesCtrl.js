'use strict';

/**
 * Responses Job (care-seeker) controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsResponsesCtrl', ['$scope', 'apiService', 'userSession', '$stateParams', '$window',
    function ($scope, apiService, userSession, $stateParams, $window) {

        $scope.responses = {};

        /**
         * Populates $scope with details about the job and caregiver that have responded.
         *
         * @returns void
         */
        var getJobResponsesHelper = new HL.CtrlHelper();
        function getJobResponses() {
            getJobResponsesHelper.success = function (data, status, headers, config) {
                $scope.job = data;
                /**
                 * For each response get caregiver details
                 *
                 * @returns void
                 */
                $scope.responses = [];
                var nosOfApplicants = $scope.job.applicants.length;
                for (var i=0; i < nosOfApplicants; i++){
                    var accountDetail = {};
                    var getAccountDetailsHelper = new HL.CtrlHelper();
                    getAccountDetailsHelper.success = function (data, status, headers, config) {
                        accountDetail = data;
                        $scope.responses.push(accountDetail);
                    };
                    apiService.Accounts.get($scope.job.applicants[i].account_id, getAccountDetailsHelper);

                };
            };
            apiService.Jobs.get($stateParams.jobID, getJobResponsesHelper);
        };
        getJobResponses();

        /**
         * select caregiver for the job
         *
         * @returns void
         */
        $scope.selectCaregiver = function(caregiverID){
            var model = {
                "job_id": $stateParams.jobID,
                "caregiver_id": caregiverID
            }
            console.log("model " + model);
            var selectCaregiverResponsesHelper = new HL.CtrlHelper();
            selectCaregiverResponsesHelper.success = function (model, status, headers, config) {
                $window.location.href("/jobs#/upcoming");
            };
            apiService.Jobs.select_applicant(model, getJobResponsesHelper);

        };


    }]);
