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

        Messages.inbox = function (data, ctrlHelper) {
            apiRequest('GET', 'messages/inbox', data, ctrlHelper, true);
        };

        Messages.thread = function (id, ctrlHelper) {
            apiRequest('GET', 'messages/thread/' + id, {}, ctrlHelper, true);
        };

        Messages.new = function (data, ctrlHelper) {
            apiRequest('POST', 'messages/new', data, ctrlHelper, true);
        };

        Messages.send = function (data, ctrlHelper) {
            apiRequest('POST', 'messages/send', data, ctrlHelper, true);
        };

        Messages.leave = function (data, ctrlHelper) {
            apiRequest('POST', 'messages/leave', data, ctrlHelper, true);
        };

        Messages.hide = function (data, ctrlHelper) {
            apiRequest('POST', 'messages/hide', data, ctrlHelper, false);
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
