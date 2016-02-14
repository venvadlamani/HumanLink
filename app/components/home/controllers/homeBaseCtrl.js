'use strict';

/**
 * Base controller for the home module.
 */
angular
    .module('Home')
    .controller('homeBaseCtrl', ['$scope', '$window', function ($scope, $window) {

        // CtrlHelper that is shared between the parent and all children.
        $scope.ctrlHelper = new HL.CtrlHelper();

        $scope.searchResults = [
            {
                'name': 'Ven Vadlamani',
                'phone': '(773) 844 - 7312'
            },
            {
                'name': 'Smita Vadlamani',
                'phone': '(773) 844 - 7311'
            },
        ];

        /**
         * Go back to the previous page/view.
         * @return void
         */
        $scope.previous = function () {
            $window.history.back();
        };

        $scope.find = function (model) {

        };

    }]);
