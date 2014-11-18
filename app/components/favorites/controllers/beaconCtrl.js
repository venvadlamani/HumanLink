'use strict';

/**
 * Controller for page which deals with sending beacons to favotire groups.
 */
angular
    .module('Favorites')
    .controller('beaconCtrl', ['$scope', function ($scope) {

        /**
         * Sends beacon to all users in given favorite
         *
         * @returns void
         */
        $scope.sendBeacon = function () {
            console.log('sendBeacon');
        };
    }]);

