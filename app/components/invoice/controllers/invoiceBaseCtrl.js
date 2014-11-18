'use strict';

/**
 * Base controller for the Invoice module.
 */
angular
    .module('Invoice')
    .controller('invoiceBaseCtrl', ['$scope', function ($scope) {

        /**
         * Populates $scope with current invoices.
         *
         * @return void
         */
        $scope.getInvoices = function () {
            console.log('getInvoices');
        };

        /**
         * Creates a new invoice.
         *
         * @return void
         */
        $scope.createInvoice = function () {
            console.log('createInvoice');
        };
    }]);
