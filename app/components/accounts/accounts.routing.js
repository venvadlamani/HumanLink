'use strict';

angular
    .module('Accounts', ['ui.router', 'ui.bootstrap', 'checklist-model', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
            // Otherwise redirect to /
            $urlRouterProvider.otherwise('/');

            $stateProvider
                .state('login', {
                    url: '/',
                    templateUrl: '/views/accounts/partials/login.html',
                    controller: 'loginCtrl',
                    data: {
                        requireLogin: false
                    }
                })
                .state('login.page', {
                    url: 'redirect/:page',
                    templateUrl: '/views/accounts/partials/login.html',
                    controller: 'loginCtrl',
                    data: {
                        requireLogin: false
                    }
                })
                .state('join', {
                    url: '/join',
                    templateUrl: '/views/accounts/partials/join.html',
                    controller: 'joinCtrl',
                    data: {
                        requireLogin: false,
                    }
                })
                .state('profile', {
                    url: '/profile',
                    templateUrl: '/views/accounts/partials/profile.html',
                    controller: 'manageProfileCtrl',
                    data: {
                        requireLogin: true
                    }
                })
                .state('settings', {
                    templateUrl: '/views/accounts/partials/settings/base_settings.html',
                })
                .state('settings.profile', {
                    url: '/settings/profile',
                    templateUrl: '/views/accounts/partials/settings/profile.html',
                    controller: 'settingsProfileCtrl',
                    data: {
                        requireLogin: true
                    }
                })
                .state('settings.caregiver', {
                    url: '/settings/caregiver',
                    templateUrl: '/views/accounts/partials/settings/caregiver.html',
                    controller: 'settingsCaregiverCtrl',
                    data: {
                        requireLogin: true
                    }
                })
                .state('settings.media', {
                    url: '/settings/media',
                    templateUrl: '/views/accounts/partials/settings/media.html',
                    controller: 'settingsMediaCtrl',
                    data: {
                        requireLogin: true
                    }
                })
                .state('settings.verification', {
                    url: '/settings/verification',
                    templateUrl: '/views/accounts/partials/settings/verification.html',
                    controller: 'settingsVerificationCtrl',
                    data: {
                        requireLogin: true
                    }
                })
                .state('settings.references', {
                    url: '/settings/references',
                    templateUrl: '/views/accounts/partials/settings/references.html',
                    controller: 'settingsReferencesCtrl',
                    data: {
                        requireLogin: true
                    }
                })
                .state('settings.reviews', {
                    url: '/settings/reviews',
                    templateUrl: '/views/accounts/partials/settings/reviews.html',
                    controller: 'settingsReviewsCtrl',
                    data: {
                        requireLogin: true
                    }
                });
        }
    ]);