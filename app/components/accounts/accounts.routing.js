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
            .state('reset', {
                url: '/reset',
                templateUrl: '/views/accounts/partials/reset.html',
                controller: 'resetCtrl',
                data: {
                    role: userSessionProvider.roles.GUEST
                }
            })
            .state('reset_password', {
                url: '/reset_password',
                templateUrl: '/views/accounts/partials/reset_password.html',
                controller: 'resetPasswordCtrl',
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
            .state('settings.seeker', {
                url: '/settings/seeker',
                templateUrl: '/views/accounts/partials/settings/seeker.html',
                controller: 'settingsSeekerCtrl'
            })
            .state('settings.seeker_preview', {
                url: '/settings/seeker_preview',
                templateUrl: '/views/accounts/partials/settings/seeker_preview.html',
                controller: 'settingsSeekerCtrl'
            })
            .state('provider', {
                abstract: true,
                templateUrl: '/views/accounts/partials/settings/base_settings_provider.html',
                data: {
                    role: userSessionProvider.roles.AUTHORIZED
                }
            })
            .state('provider.caregiver', {
                url: '/settings/caregiver',
                templateUrl: '/views/accounts/partials/settings/caregiver.html',
                controller: 'settingsProfileCaregiverCtrl'
            })
            .state('provider.preview', {
                url: '/settings/preview',
                templateUrl: '/views/accounts/partials/settings/provider_preview.html',
                controller: 'previewProfileCtrl'
            })
            .state('provider.media', {
                url: '/settings/media',
                templateUrl: '/views/accounts/partials/settings/media.html',
                controller: 'settingsMediaCtrl'
            })
            .state('provider.verification', {
                url: '/settings/verification',
                templateUrl: '/views/accounts/partials/settings/verification.html',
                controller: 'settingsVerificationCtrl'
            });
    }

})();
