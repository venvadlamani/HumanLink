'use strict';

/**
 * API Service that talks to the backend.
 */
angular
    .module('Common')
    .factory('apiService', ['$http', function ($http) {

        // Google Cloud Endpoints URL.
        var getGceBase = function() {
            var host = window.location.host;
            var protocol = host.indexOf('localhost') === 0 ? 'http://' : 'https://';
            return protocol + host + '/_ah/api/humanlink/v1/';
        };

        var GCE_BASE = getGceBase();

        var Accounts = {};
        var Billing = {};
        var Connections = {};
        var Jobs = {};
        var Messages = {};
        var Notifications = {};

        /**
         * Base method to communicate with the APIs.
         *
         * @param method : 'GET' or 'POST'
         * @param uri : relative path to the base URL or GCE URL
         * @param data : request data
         * @param ctrlHelper : CtrlHelper with callbacks
         * @param useEndpoints : whether this is a GCE API or not.
         */
        var apiRequest = function (method, uri, data, ctrlHelper, useEndpoints) {
            ctrlHelper.isLoading = true;
            ctrlHelper.isValid = true;
            ctrlHelper.errors = [];

            // Use endpoints by default.
            if (!angular.isDefined(useEndpoints)) {
                useEndpoints = true;
            }

            $http({
                method: method,
                url: (useEndpoints ? GCE_BASE : '/') + uri,
                data: data
            })
            .success(function (data, status, headers, config) {
                ctrlHelper.isLoading = false;
                if (angular.isFunction(ctrlHelper.success)) {
                    ctrlHelper.success(data, status, headers, config);
                }
                if (angular.isFunction(ctrlHelper.always)) {
                    ctrlHelper.always(data, status, headers, config);
                }
            })
            .error(function (data, status, headers, config) {
                ctrlHelper.isLoading = false;
                if (angular.isFunction(ctrlHelper.failure)) {
                    ctrlHelper.failure(data, status, headers, config);
                }
                if (angular.isFunction(ctrlHelper.always)) {
                    ctrlHelper.always(data, status, headers, config);
                }
            });
        };

        Accounts.login = function (data, ctrlHelper) {
            apiRequest('POST', 'login', data, ctrlHelper, false);
        };

        Accounts.signup = function (data, ctrlHelper) {
            apiRequest('POST', 'signup', data, ctrlHelper, false);
        };

        // Public methods.
        return {
            Accounts: Accounts,
            Billing: Billing,
            Connections: Connections,
            Jobs: Jobs,
            Messages: Messages,
            Notifications: Notifications
        };

    }]);
