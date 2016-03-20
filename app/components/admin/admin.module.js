'use strict';

/**
 * Admin module.
 */
(function () {
    angular
        .module('Admin', [
            'ui.bootstrap',
            'checklist-model',
            'Common'
        ])
        .config(Config);

    /** ngInject */
    function Config($stateProvider, $urlRouterProvider, userSessionProvider) {

        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('admin', {
                abstract: true,
                templateUrl: '/views/admin/partials/base_admin.html',
                data: {
                    role: userSessionProvider.roles.AUTHORIZED
                }
            })
            .state('admin.verification', {
                url: '/verification',
                templateUrl: '/views/admin/partials/verification.html',
                controller: 'verificationCtrl'
            })
            .state('admin.seeker', {
                url: '/seeker',
                templateUrl: '/views/admin/partials/seeker.html',
                controller: 'seekerCtrl'
            })
            .state('admin.provider', {
                url: '/provider',
                templateUrl: '/views/admin/partials/provider.html',
                controller: 'providerCtrl'
            })
            .state('admin.password', {
                url: '/password',
                templateUrl: '/views/admin/partials/password.html',
                controller: 'passwordCtrl'
            });
    }

})();
