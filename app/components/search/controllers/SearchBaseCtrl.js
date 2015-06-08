'use strict';

(function () {
    angular
        .module('Search')
        .controller('SearchBaseCtrl', Ctrl);

    /** ngInject */
    function Ctrl($scope,$window,$location){
        // call SearchMain partials
        $location.path('/search');
    }
})();
