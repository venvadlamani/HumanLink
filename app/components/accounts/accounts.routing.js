'use strict';

/**
 * Accounts module.
 */
(function () {
    angular
        .module('Accounts', [
            'ui.bootstrap',
            'checklist-model',
            'Common'
        ])
        .config(Config);

    /** ngInject */
    function Config($stateProvider, $urlRouterProvider, userSessionProvider) {

        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('login', {
                url: '/?next',
                templateUrl: '/views/accounts/partials/login.html',
                controller: 'loginCtrl',
                data: {
                    role: userSessionProvider.roles.GUEST
                }
            })
            .state('join', {
                url: '/join',
                templateUrl: '/views/accounts/partials/join.html',
                controller: 'joinCtrl',
                data: {
                    role: userSessionProvider.roles.GUEST
                }
            })
            .state('profile', {
                url: '/profile',
                templateUrl: '/views/accounts/partials/profile.html',
                controller: 'manageProfileCtrl',
                data: {
                    role: userSessionProvider.roles.AUTHORIZED
                }
            })
            .state('settings', {
                abstract: true,
                templateUrl: '/views/accounts/partials/settings/base_settings.html',
                data: {
                    role: userSessionProvider.roles.AUTHORIZED
                }
            })
            .state('settings.profile', {
                url: '/settings/profile',
                templateUrl: '/views/accounts/partials/settings/profile.html',
                controller: 'settingsProfileCtrl'
            })
            .state('settings.caregiver', {
                url: '/settings/caregiver',
                templateUrl: '/views/accounts/partials/settings/caregiver.html',
                controller: 'settingsProfileCaregiverCtrl'
            })
            .state('settings.media', {
                url: '/settings/media',
                templateUrl: '/views/accounts/partials/settings/media.html',
                controller: 'settingsMediaCtrl'
            })
            .state('settings.preview', {
                url: '/settings/preview',
                templateUrl: '/views/accounts/partials/profile.html',
                controller: 'manageProfileCtrl'
            })
            .state('settings.sample', {
                url: '/settings/sample',
                templateUrl: '/views/accounts/partials/sample_profile.html',
            })
            .state('settings.verification', {
                url: '/settings/verification',
                templateUrl: '/views/accounts/partials/settings/verification.html',
                controller: 'settingsVerificationCtrl'
            });
    }

})();
