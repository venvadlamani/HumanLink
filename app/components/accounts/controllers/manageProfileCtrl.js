'use strict';

/**
 * Controller for account management page
 */
angular
    .module('Accounts')
    .controller('manageProfileCtrl', ['$scope', function ($scope) {

        /**
         * Add's patient under current account.
         *
         * @return void
         */
        $scope.addPatient = function () {
            console.log('addPatient');
        };
    }]);
