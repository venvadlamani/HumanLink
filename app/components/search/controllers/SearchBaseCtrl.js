'use strict';

(function () {
    angular
        .module('Search')
        .controller('SearchBaseCtrl', ['$scope','$window','$location',function($scope,$window,$location){
            // call SearchMain partials
            $location.path('/search');
        }]);

    /** ngInject */
    function Ctrl($scope) { /* Empty. */ }
})();
