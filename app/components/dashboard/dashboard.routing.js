'use strict';

angular
    .module('Dashboard', ['ui.router', 'ui.bootstrap', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
            function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/views/dashboard/partials/dashboard.html',
            })
    }]);
