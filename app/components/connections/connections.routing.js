'use strict';

angular
    .module('Connections', ['ui.router', 'ui.bootstrap', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
        function ($stateProvider, $urlRouterProvider) {

            // Otherwise redirect to /
            $urlRouterProvider.otherwise('/');

            $stateProvider
                .state('home', {
                    url: '/',
                    templateUrl: '/views/connections/partials/all.html'
                })
                .state('all', {
                    url: '/all',
                    templateUrl: '/views/connections/partials/all.html',
                    controller: 'connectionsBaseCtrl'
                })
                .state('favorites', {
                    url: '/favorites',
                    templateUrl: '/views/connections/partials/favorites.html',
                    controller: 'connectionsBaseCtrl'
                })
                .state('pending', {
                    url: '/pending',
                    templateUrl: '/views/connections/partials/pending.html',
                    controller: 'connectionsPendingCtrl'
                })
        }]);
