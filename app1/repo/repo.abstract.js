(function () {
    'use strict';

    angular
        .module('app.repo')
        .factory('AbstractRepo', AbstractRepo);

    /** ngInject */
    function AbstractRepo($http, $q, Config) {

        return {
            get: get,
            post: post
        };

        function get(uri, data, isApi) {
            return httpRequest('GET', uri, data, isApi);
        }

        function post(uri, data, isApi) {
            return httpRequest('POST', uri, data, isApi);
        }

        function httpRequest(method, uri, data, isApi) {
            isApi = angular.isDefined(isApi) ? isApi : true;
            return $http({
                method: method,
                url: (isApi ? Config.api_base : '/') + uri,
                data: data
            });
        }

    }

})();
