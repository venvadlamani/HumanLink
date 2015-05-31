'use strict';

/**
 * Search module.
 */
angular
    .module('Search', ['ui.router', 'ui.bootstrap', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
        function ($stateProvider, $urlRouterProvider) {

            // Otherwise redirect to /
            $urlRouterProvider.otherwise('/');

            $stateProvider
                .state('search', {
                    url: '/',
                    templateUrl: '/views/search/partials/search.html',
                    controller: 'SearchMainCtrl'
                });
        }]);
