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
            .state('admin.guest', {
                abstract: true,
                templateUrl: '/views/admin/partials/guest.html',
            })
            .state('admin.guest.child', {
                url: '/guest',
                views: {
                    '': {templateUrl: '/views/accounts/partials/settings/caregiver.html'}
                },
                controller: 'guestCtrl'
            })
            .state('admin.invite', {
                url: '/invite',
                templateUrl: '/views/admin/partials/invite.html',
                controller: 'inviteCtrl'
            })
            .state('admin.password', {
                url: '/password',
                templateUrl: '/views/admin/partials/password.html',
                controller: 'passwordCtrl'
            });
    }

})();
