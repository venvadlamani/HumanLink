'use strict';

/**
 * Base controller for the home module.
 */
angular
    .module('Home')
    .controller('homeBaseCtrl', ['$scope', '$window', function ($scope, $window) {

        // CtrlHelper that is shared between the parent and all children.
        $scope.ctrlHelper = new HL.CtrlHelper();

        /**
         * Go back to the previous page/view.
         * @return void
         */
        $scope.previous = function () {
            $window.history.back();
        };

    }]);
