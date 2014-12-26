'use strict';

/**
 * Update Job (care-seeker) controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsUpdateCtrl', ['$scope', 'apiService', 'userSession', '$stateParams',
    function ($scope, apiService, userSession, $stateParams) {

        // Possible ng-switch values.
        var viewModes = ['post_job', 'post_job_success'];
        $scope.viewMode = viewModes[0];

        /*
         ** initialize the screen with  job details
         */
        $scope.job ={};

        var getJobsHelper = new HL.CtrlHelper();
        function getJobDetails() {
            getJobsHelper.success = function (data, status, headers, config) {
                $scope.job = data;

                //get the dates and hours
                $scope.job.caredate = new Date($scope.job.start_date);
                var tmpStartDate = new Date ($scope.job.start_date);
                var tmpEndDate = new Date ($scope.job.end_date);

                if (tmpStartDate.getHours()>12){
                    $scope.job.startHour = String(tmpStartDate.getHours() - 12);
                    $scope.job.ampm = "PM";
                } else {
                    $scope.job.startHour = String(tmpStartDate.getHours());
                    $scope.job.ampm = "AM";
                };

                if (tmpStartDate.getMinutes() === 0){
                    $scope.job.startMinute = "00";
                } else {
                    $scope.job.startMinute = "30";
                };
                $scope.job.hours = (tmpEndDate - tmpStartDate)/3600000;
            };
            apiService.Jobs.get($stateParams.jobID, getJobsHelper);
        };
        getJobDetails();

        $scope.initData = {
            "careRecipients":       [{
                                        'careRecipientId' : '1',
                                        'firstName' : 'Pop-pop',
                                        'lastName' : 'Matthrews',
                                        'recipientAddress' : '1940 North Honore Street, Chicago, IL 60622, USA',
                                        'recipientStreet' : '1940 Marshfield drive',
                                        'recipientCity' : 'Chicago',
                                        'recipientState' : 'IL',
                                        'recipientZipcode' : '60612',
                                        'recipientCreditCard' : '5555 5555 5555 5555',
                                        'recipientCardExpiryMonth' : '12',
                                        'recipientCardExpiryYear' : '2017'
                                    },
                                    {
                                        'careRecipientId' : '2',
                                        'firstName' : 'Nanna',
                                        'lastName' : 'Jupiter',
                                        'recipientAddress' : '42 South Main Street, Bentonville, AR 72712, USA',
                                        'recipientStreet' : '42 South Main Street',
                                        'recipientCity' : 'Bentonville',
                                        'recipientState' : 'AR',
                                        'recipientZipcode' : '72712',
                                        'recipientCreditCard' : '2222 2222 2222 2222',
                                        'recipientCardExpiryMonth' : '12',
                                        'recipientCardExpiryYear' : '2017'
                                    }],

            "audienceOptions":      ["Connection", "Favorites",  "Community"],
            "hours":                ['1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12'],
            "minutes":              ['00', '30'],
            "ampm":                 ['AM', 'PM']
        };

        $scope.toggleMin = function() {
            $scope.minDate = $scope.minDate ? null : new Date();
        };
        $scope.toggleMin();

        /*
         ** update job
         */
        var jobsUpdateHelper = new HL.CtrlHelper();
        $scope.updateJob = function(model) {

            alert("update job functionality is not available currently");
            /**
            //set the job.start_date fields
            var tempStartDate = new Date($scope.job.caredate);
            if( $scope.job.ampm === 'AM' ) {
                tempStartDate.setHours( parseInt($scope.job.startHour) );
            } else {
                tempStartDate.setHours( parseInt($scope.job.startHour) + 12);
            };
            tempStartDate.setMinutes( parseInt($scope.job.startMinute) );
            tempStartDate.setSeconds(0);

            //set the job.start_date fields
            $scope.job.start_date = tempStartDate;

            //set the job.end_date fields
            var tempEndDate = new Date(tempStartDate);
            if($scope.job.hours) {
                tempEndDate.setHours(tempEndDate.getHours() + parseInt($scope.job.hours));
                $scope.job.end_date = tempEndDate;
            };

            jobsUpdateHelper.success = function (data, status, headers, config) {
                $scope.viewMode = viewModes[1];
            };
            apiService.Jobs.update(model, jobsUpdateHelper);
            **/

        };

    }]);
