'use strict';

/**
 * Settings module.
 */
(function () {
    angular
        .module('Settings', [
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
            .state('settings', {
                abstract: true,
                templateUrl: '/views/settings/partials/base_settings.html',
            })
            .state('settings.security', {
                url: '/',
                templateUrl: '/views/settings/partials/security.html',
                controller: 'securityCtrl'
            })
            .state('settings.payments', {
                url: '/payments',
                templateUrl: '/views/settings/partials/payments.html',
                controller: 'paymentsCtrl'
            })
            .state('settings.notifications', {
                url: '/notifications',
                templateUrl: '/views/settings/partials/notifications.html',
                controller: 'notificationsCtrl'
            });
    }

})();
