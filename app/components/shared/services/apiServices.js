'use strict';

/**
 * API Service that talks to the backend.
 */
angular
    .module('Common')
    .factory('apiService', ['$http', function ($http) {

        // Google Cloud Endpoints URL.
        var getGceBase = function () {
            var host = window.location.host;
            // GCE doesn't work with custom domains.
            if (host.indexOf('humanlink.co') === 0) {
                host = 'care-tiger.appspot.com';
            }
            var protocol = host.indexOf('localhost') === 0 ? 'http://' : 'https://';
            return protocol + host + '/_ah/api/humanlink/v1/';
        };

        var GCE_BASE = getGceBase();

        var Accounts = {
            patients: {}
        };
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
            apiRequest('POST', 'login.json', data, ctrlHelper, false);
        };

        Accounts.signup = function (data, ctrlHelper) {
            apiRequest('POST', 'signup.json', data, ctrlHelper, false);
        };

        Accounts.userdata = function (data, ctrlHelper) {
            apiRequest('GET', 'accounts/userdata.json', data, ctrlHelper, false);
        };

        Accounts.get = function (id, ctrlHelper) {
            apiRequest('GET', 'accounts/' + id, {}, ctrlHelper, true);
        };

        Accounts.patients.list = function (ctrlHelper) {
            apiRequest('GET', 'accounts/patients/list', {}, ctrlHelper, true);
        };

        Connections.my = function (data, ctrlHelper) {
            apiRequest('GET', 'connections/my', data, ctrlHelper, true);
        };

        Jobs.get = function(id, ctrlHelper){
            apiRequest('GET', 'jobs/' + id, {}, ctrlHelper, true);
        };

        Jobs.cancel = function(data, ctrlHelper){
            apiRequest('POST', 'jobs/cancel', data, ctrlHelper, true);
        };

        Jobs.update = function(data, ctrlHelper){
            apiRequest('POST', 'jobs/update', data, ctrlHelper, true);
        };

        Jobs.select_applicant = function(data, ctrlHelper){
            apiRequest('POST', 'jobs/select_applicant', data, ctrlHelper, true);
        };

        Jobs.posted = function(data, ctrlHelper){
            apiRequest('GET', 'jobs/posted', data, ctrlHelper, true);
        };

        Jobs.selected = function(data, ctrlHelper){
            apiRequest('GET', 'jobs/selected', data, ctrlHelper, true);
        };

        Jobs.applied = function(data, ctrlHelper){
            apiRequest('GET', 'jobs/applied', data, ctrlHelper, true);
        };

        Jobs.nearby = function(data, ctrlHelper){
            apiRequest('GET', 'jobs/nearby', data, ctrlHelper, true);
        };

        Jobs.apply = function(data, ctrlHelper){
            apiRequest('POST', 'jobs/apply', data, ctrlHelper, true);
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
