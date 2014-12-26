'use strict';

/**
 * Create Job controller for the Jobs module.
 */
angular
    .module('Jobs')
    .controller('jobsCreateCtrl', ['$scope', '$window', '$stateParams', 'apiService', '$http',
    function ($scope, $window, $stateParams, apiService, $http) {

        // Possible ng-switch values.
        var viewModes = ['post_job', 'post_job_success'];
        $scope.viewMode = viewModes[0];

        /*
         ** Initialize form
         */
        $scope.job = {};
        $scope.initData = {
            "careRecipients":       [{
                                        'careRecipientId' : 1,
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
                                        'careRecipientId' : 2,
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
            "certificates":          ['Caregiver', 'CNA (Certified Nursing Assistant)', 'LPN (Licensed Practical Nurse)'],
            "ampm":                 ['AM', 'PM']
        };

        $scope.toggleMin = function() {
            $scope.minDate = $scope.minDate ? null : new Date();
        };
        $scope.toggleMin();

        if ( !$scope.job.startHour ){
            $scope.job.startHour = "8";
        };
        if ( !$scope.job.startMinute ){
            $scope.job.startMinute = "00";
        };
        if ( !$scope.job.ampm ){
            $scope.job.ampm = "AM";
        };

        $scope.startEndDates = function() {

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
        };

        /*
         ** Post job
         */
        var jobsHelper = new HL.CtrlHelper();
        $scope.submitJob = function(model, isValid) {

            if(isValid){
                jobsHelper.success = function (data, status, headers, config) {
                    $scope.viewMode = viewModes[1];
                };
                apiService.Jobs.update(model, jobsHelper);
            } else {
                console.log("there are errors");
            };
        };

    }]);
