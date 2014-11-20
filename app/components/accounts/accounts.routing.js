'use strict';

angular
    .module('Accounts', ['ui.router', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('login', {
                url: '/',
                templateUrl: '/views/accounts/partials/login.html',
                controller: 'loginCtrl'
            })
            .state('join', {
                url: '/join',
                templateUrl: '/views/accounts/partials/join.html',
                controller: 'joinCtrl'
            })
            .state('profile', {
                url: '/profile',
                templateUrl: '/views/accounts/partials/profile.html'
            });
    }]);
