'use strict';

/**
 * Details controller for the Connections module.
 */
angular
    .module('Connections')
    .controller('connectionDetailsCtrl', ['$scope', '$window', '$stateParams', function ($scope, $window, $stateParams) {    	
    	
    	console.log('connectionDetailsCtrl');
    	$scope.connectionId = $stateParams.connectionId;    	
    	
    }]);    	