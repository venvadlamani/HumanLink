(function () {
    'use strict';

    angular
        .module('app.repo')
        .factory('SettingsRepo', SettingsRepo);

    /** ngInject */
    function SettingsRepo($q, $log, AbstractRepo) {

        var cache = {
            settings: null
        };

        return {
            addPayment: addPayment,
            changePassword: changePassword,
            closeAccount: closeAccount,
            deletePayment: deletePayment,
            getSettings: getSettings,
            updateNotifications: updateNotifications
        };

        function getSettings(forceRemote) {
            if (!cache.settings || forceRemote) {
                cache.settings = dummyData();
            }
            return $q.when(cache.settings);
        }

        function changePassword(oldValue, newValue) {
            $log.debug([oldValue, newValue].join(', '));
            $log.debug('changePassword not implemented.');
        }

        function updateNotifications(notifications) {
            $log.debug(notifications);
            $log.debug('updateNotifications not implemented');
        }

        function addPayment(payment) {
            $log.debug(payment);
            $log.debug('addPayment not implemented.');
        }

        function deletePayment() {
            $log.debug('deletePayment not implemented.');
        }

        function closeAccount(reason) {
            $log.debug(reason);
            $log.debug('closeAccount not implemented.');
        }

        function dummyData() {
            var settings = {
                notifications: {
                    logins: false,
                    messages: true,
                    company_updates: true,
                    request_reminders: true,
                    request_updates: true
                },
                payment: {
                    card_type: 'visa',
                    last_four: '4242'
                }
            };
            return settings;
        }
    }

})();
