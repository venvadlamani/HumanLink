'use strict';

/**
 * Base controller for the Invoice module.
 */
angular
    .module('Invoice')
    .controller('invoiceDetailCtrl', ['$scope', 'apiService', 'userSession', '$stateParams',
    function ($scope, apiService, userSession, $stateParams) {

        /**
         * Populates $scope with invoice for the selected job.
         *
         * @return void
         */
            $scope.jobID = $stateParams.jobID;

    }]);
