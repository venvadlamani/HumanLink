/**
 * Settings module.
 */
(function () {
    'use strict';

    angular
        .module('app.settings', [
            'app.core',
            'app.repo',
            'Common'
        ])
        .config(Config);

    /** ngInject */
    function Config($stateProvider, $urlRouterProvider, userSessionProvider) {

        $urlRouterProvider.otherwise('/notifications');

        $stateProvider
            .state('settings', {
                abstract: true,
                views: {
                    '': {
                        templateUrl: '/views/settings/partials/main.html',
                        controller: 'Base',
                        controllerAs: 'base'
                    },
                    'loader@settings': {
                        templateUrl: '/views/settings/partials/loader.html'
                    }
                }
            })
            .state('settings.notifications', {
                url: '/notifications',
                templateUrl: '/views/settings/partials/notifications.html',
                controller: 'Notifications',
                controllerAs: 'vm'
            })
            .state('settings.payments', {
                url: '/payments',
                template: 'payments'
            })
            .state('settings.transactions', {
                url: '/transactions',
                template: 'transactions'
            })
            .state('settings.security', {
                url: '/security',
                template: 'security'
            })
            .state('settings.close', {
                url: '/close',
                template: 'close account'
            });
    }

})();
