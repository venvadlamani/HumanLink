'use strict';

(function () {
    angular
        .module('Search')
        .controller('SearchMainCtrl', Ctrl);

    /** @ngInject */
    function Ctrl($scope, $state, $stateParams) {
        $scope.title = 'Hello';
    }
})();
