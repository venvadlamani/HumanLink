'use strict';

angular
    .module('Favorites', ['ui.router','ui.bootstrap', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
            function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/views/favorites/partials/favorites.html',
            })

            .state('send_beacon', {
                url: '/send_beacon',
                templateUrl: '/views/favorites/partials/send_beacon.html',
                controller: 'beaconCtrl'
            });
    }]);

