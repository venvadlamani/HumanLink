'use strict';

/**
 * Base controller for the Collections module.
 */
angular
    .module('Favorites')
    .controller('favoritesBaseCtrl', ['$scope', function ($scope) {

        /**
         * Obtains all favorites.
         *
         * @returns void
         */
        $scope.getFavorites = function () {
            console.log('getFavorites');
        };
    }]);

