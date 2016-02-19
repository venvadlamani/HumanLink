'use strict';

/**
 * Payments controller
 */
angular
    .module('Settings')
    .controller('paymentsCtrl', ['$scope', '$http', function ($scope, $http) {

        $scope.paymentModel = {};

        var init = function () {
            $scope.paymentModel.plan = 'basic';
        };
        init();

    }]);
