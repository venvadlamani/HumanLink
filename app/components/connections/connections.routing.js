'use strict';

angular
    .module('Connections', ['ui.router','ui.bootstrap', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
    function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/views/connections/partials/connections.html'
            })
    }]);
