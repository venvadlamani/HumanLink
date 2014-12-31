'use strict';

angular
    .module('Accounts', ['ui.router', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
            function ($stateProvider, $urlRouterProvider) {

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
            .state('edit_profile', {
                url: '/edit',
                templateUrl: '/views/accounts/partials/manage_profile.html',
                controller: 'manageProfileCtrl'
            })
            .state('caregiver_profile', {
                url: '/caregiver',
                templateUrl: '/views/accounts/partials/caregiver_profile.html',
                controller: 'caregiverProfileCtrl'
            });
    }]);
