(function () {
    'use strict';

    angular
        .module('app.common')
        .factory('CommonService', CommonService);

    /** ngInject */
    function CommonService($q, $rootScope) {

        return {
            broadcast: broadcast,
            on: on
        };

        /**
         * Broadcasts an event at the `$rootScope` level.
         * Alias to `$rootScope.$broadcast`.
         */
        function broadcast() {
            return $rootScope.$broadcast.apply($rootScope, arguments);
        }

        /**
         * Listens to a given event at the `$rootScope` level.
         * Alias to `$rootScope.$on`.
         */
        function on() {
            return $rootScope.$on.apply($rootScope, arguments);
        }

    }

})();
