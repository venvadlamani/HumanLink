'use strict';
angular
    .module('Jobs', ['ui.router','ui.bootstrap','Common'])
    .config(['$stateProvider', '$urlRouterProvider',
    function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/views/jobs/partials/upcoming.html',
                controller: 'jobsUpcomingCtrl'
            })
            .state('upcoming', {
                url: '/upcoming',
                templateUrl: '/views/jobs/partials/upcoming.html',
                controller: 'jobsUpcomingCtrl'
            })
            .state('previous', {
                url: '/previous',
                templateUrl: '/views/jobs/partials/previous.html',
                controller: 'jobsPreviousCtrl'
            })
            .state('pending', {
                url: '/pending',
                templateUrl: '/views/jobs/partials/pending.html',
                controller: 'jobsPendingCtrl'
            })
            .state('applied', {
                url: '/applied',
                templateUrl: '/views/jobs/partials/applied.html',
                controller: 'jobsAppliedCtrl'
            })
            .state('selected', {
                url: '/selected',
                templateUrl: '/views/jobs/partials/selected.html',
                controller: 'jobsSelectedCtrl'
            })
            .state('completed', {
                url: '/completed',
                templateUrl: '/views/jobs/partials/completed.html',
                controller: 'jobsCompletedCtrl'
            })
            .state('nearby', {
                url: '/nearby',
                templateUrl: '/views/jobs/partials/nearby.html',
                controller: 'jobsNearbyCtrl'
            })            
            .state('responses', {
                url: '/responses/{jobID}',
                templateUrl: '/views/jobs/partials/responses.html',
                controller: 'jobsResponsesCtrl'
            })
            .state('update', {
                url: '/update/{jobID}',
                templateUrl: '/views/jobs/partials/update.html',
                controller: 'jobsUpdateCtrl'
            })
            .state('create', {
                url: '/create/create',
                templateUrl: '/views/jobs/partials/create/create.html',
                controller: 'jobsCreateCtrl'
            })
            .state('create.who', {
                url: '/who',
                templateUrl: '/views/jobs/partials/create/who.html'
            })
            .state('create.when', {
                url: '/when',
                templateUrl: '/views/jobs/partials/create/when.html'
            })
            .state('create.audience', {
                url: '/audience',
                templateUrl: '/views/jobs/partials/create/audience.html'
            })
            .state('create.payment', {
                url: '/payment',
                templateUrl: '/views/jobs/partials/create/payment.html'
            })
            .state('create.notes', {
                url: '/notes',
                templateUrl: '/views/jobs/partials/create/notes.html'
            })
            .state('create.confirm', {
                url: '/confirm',
                templateUrl: '/views/jobs/partials/create/confirm.html'
            })
            .state('jobco', {
                url: '/jobco',
                templateUrl: '/views/jobs/partials/jobco.html'
            })
            ;
    }]);
