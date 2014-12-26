'use strict';

/**
 * Controller for account management page
 */
angular
    .module('Accounts')
    .controller('manageProfileCtrl', ['$scope', function ($scope) {
        $scope.patients = [
            {name: 'Patient Name', phone: '(555)555-5555'},
            {name: 'Patient Name', phone: '(555)555-5555'},
            {name: 'Patient Name', phone: '(555)555-5555'},
            {name: 'Patient Name', phone: '(555)555-5555'}
        ];

        /**
         * Add's patient under current account.
         *
         * @return void
         */
        $scope.addPatient = function () {
            console.log('addPatient');
        };
    }]);
