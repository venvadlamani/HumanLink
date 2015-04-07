'use strict';

angular
    .module('Invoice', ['ui.router', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
            function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/views/invoice/partials/invoice.html',
            })
            .state('detail', {
                url: '/detail/{jobID}',
                templateUrl: '/views/invoice/partials/detail.html',
                controller: 'invoiceDetailCtrl'
            });
    }]);
