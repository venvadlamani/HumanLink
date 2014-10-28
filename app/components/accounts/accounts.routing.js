angular
    .module('Accounts', ['ui.router', 'Common'])

    .config(['$stateProvider', '$urlRouterProvider', function ($stateProvider, $urlRouterProvider) {
        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');


        $stateProvider
            .state('login', {
                url: '/',
                templateUrl: '/views/accounts/partials/login.html',
            })

            .state('profile', {
                url: '/profile',
                templateUrl: '/views/accounts/partials/profile.html',
            });
    }]);
