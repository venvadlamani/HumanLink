'use strict';

angular
    .module('Messages', ['ui.router', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
    function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('inbox', {
                url: '/inbox',
                templateUrl: '/views/messages/partials/inbox.html',
                controller: 'messagesInboxCtrl'
            })
            .state('new', {
                url: '/new/{account_id}',
                templateUrl: '/views/messages/partials/new.html',
                controller: 'messagesNewCtrl'
            })
            .state('tmpnew', {
                url: '/new',
                templateUrl: '/views/messages/partials/new.html',
                controller: 'messagesNewCtrl'
            })
            .state('detail', {
                url: '/detail',
                templateUrl: '/views/messages/partials/detail.html',
                controller: 'messagesDetailCtrl'
            });
    }]);
