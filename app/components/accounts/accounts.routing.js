'use strict';

angular
    .module('Accounts', ['ui.router', 'ui.bootstrap', 'checklist-model', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
            function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('login', {
                url: '/',
                templateUrl: '/views/accounts/partials/login.html',
                controller: 'loginCtrl'
            })
            .state('join', {
                url: '/join',
                templateUrl: '/views/accounts/partials/join.html',
                controller: 'joinCtrl'
            })
            .state('profile', {
                url: '/profile',
                templateUrl: '/views/accounts/partials/profile.html',
                controller: 'manageProfileCtrl'
            })
            .state('settings', {
                templateUrl: '/views/accounts/partials/settings/base_settings.html',
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
    }]);
