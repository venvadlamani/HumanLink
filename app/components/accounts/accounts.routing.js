angular
    .module('Accounts', ['ui.router'])

    .config(function ($stateProvider, $urlRouterProvider) {
        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');


        $stateProvider
            .state('login', {
                url: '/',
                templateUrl: '/views/accounts/partials/login.html',
            });
    });
