'use strict';

/**
 * Dashboard module.
 */
(function () {
    angular
        .module('Dashboard', [
            'ui.bootstrap',
            'checklist-model',
            'Common',
            'stripe'
        ])
        .config(Config);

    /** ngInject */
    function Config($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('dashboard', {
                abstract: true,
                templateUrl: '/views/dashboard/partials/base_dashboard.html',
            })
            .state('dashboard.main', {
                url: '/',
                templateUrl: '/views/dashboard/partials/main.html',
                controller: 'mainCtrl'
            });
    }

})();
