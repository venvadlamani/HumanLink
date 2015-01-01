'use strict';

/**
 * Base controller for the Connections module.
 */
angular
    .module('Connections')
    .controller('connectionsBaseCtrl', ['$scope', '$window', function ($scope, $window) {
    	
        /**
         * Populates $scope with connections.
         *
         * @returns void
         */
    	var getConnections = function() {
            console.log('getConnections');               
            //name-value pairs
            return [
                  {
               	   'connectionId': '001',
            	   'firstName': 'Jane',
            	   'lastName': 'Q. Prototype',
            	   'imageURL': 'images/victoria-vorel.jpg',
            	   'role': 'Caregiver',
            	   'caregiverRating': '3',
            	   'tagFavorites': true},
            	  {
            	   'connectionId': '002',
				   'firstName': 'Juliet',
				   'lastName': 'P. Public',
				   'imageURL': 'images/ashley-turner.jpg',
				   'role': 'senior transitions manager',
            	   'caregiverRating': null,
				   'tagFavorites': false},
            	  {
	               'connectionId': '003',
        		   'firstName': 'Juliet 4',
        		   'lastName': 'P. Public',
        		   'imageURL': 'images/ashley-turner.jpg',
        		   'role': 'senior transitions manager',
            	   'caregiverRating': null,
        		   'tagFavorites': false},
             	  {
                   'connectionId': '004',
        		   'firstName': 'Juliet 5',
        		   'lastName': 'P. Public',
        		   'imageURL': 'images/ashley-turner.jpg',
        		   'role': 'senior transitions manager',
            	   'caregiverRating': null,
        		   'tagFavorites': false}        		   
        		   ];            
    	 };        
    	$scope.connections = getConnections();    		    		
    }]);
