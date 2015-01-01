'use strict';

angular
    .module('Connections', ['ui.router','ui.bootstrap', 'Common'])
    .config(['$stateProvider', '$urlRouterProvider',
            function ($stateProvider, $urlRouterProvider) {

        // Otherwise redirect to /
        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: '/',
                templateUrl: '/views/connections/partials/connections.html',
            })
			.state('details', {
			    url: '/details/{ connectionId }',
			    templateUrl: '/views/connections/partials/details.html',
			    controller: 'connectionsDetailsCtrl'
			});
    }]);
