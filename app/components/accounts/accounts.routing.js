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
            .state('settings.recipients', {
                url: '/settings/recipients',
                templateUrl: '/views/accounts/partials/settings/profile_careseeker.html',
                controller: 'settingsProfileCareseekerCtrl'
            })
            .state('settings.favorites', {
                url: '/settings/favorites',
                templateUrl: '/views/accounts/partials/settings/favorites.html',
                controller: 'settingsFavoritesCtrl'
            })
            .state('settings.caregiver', {
                url: '/settings/caregiver',
                templateUrl: '/views/accounts/partials/settings/caregiver.html',
                controller: 'settingsCaregiverCtrl'
            })
            .state('settings.media', {
                url: '/settings/media',
                templateUrl: '/views/accounts/partials/settings/media.html',
                controller: 'settingsMediaCtrl'
            })
            .state('settings.verification', {
                url: '/settings/verification',
                templateUrl: '/views/accounts/partials/settings/verification.html',
                controller: 'settingsVerificationCtrl'
            })
            .state('settings.references', {
                url: '/settings/references',
                templateUrl: '/views/accounts/partials/settings/references.html',
                controller: 'settingsReferencesCtrl'
            })
            .state('settings.reviews', {
                url: '/settings/reviews',
                templateUrl: '/views/accounts/partials/settings/reviews.html',
                controller: 'settingsReviewsCtrl'
            });
    }

})();
