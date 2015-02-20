'use strict';

angular
    .module('Messages', ['ui.router', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
            function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('messages', {
                templateUrl: '/views/messages/partials/messages.html'
            })
            .state('messages.inbox', {
                url: '/inbox',
                templateUrl: '/views/messages/partials/inbox.html',
                controller: 'messagesInboxCtrl'
            })
            .state('messages.detail', {
                url: '/detail',
                templateUrl: '/views/messages/partials/detail.html',
                controller: 'messagesDetailCtrl'
            })
            .state('messages.notifications', {
                url: '/notifications',
                templateUrl: '/views/messages/partials/notifications.html',
                controller: 'messagesNotificationsCtrl'
            })
            .state('messages.connections', {
                url: '/connections',
                templateUrl: '/views/messages/partials/connections.html',
                controller: 'messagesConnectionsCtrl'
            });
    }]);
