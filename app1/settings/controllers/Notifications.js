(function () {
    'use strict';

    angular
        .module('app.settings')
        .controller('Notifications', Notifications);

    /* @ngInject */
    function Notifications($scope, SettingsRepo,
                           CommonService, CommonEvents) {
        var vm = this;
        vm.settings = null;
        vm.update = update;

        init();
        function init() {
            load();
        }

        function load() {
            SettingsRepo.getSettings().then(function (data) {
                CommonService.broadcast(CommonEvents.viewReady);
                vm.notifications = data.notifications;
            });
        }

        function update(notifications) {
            SettingsRepo.updateNotifications(notifications);
        }

    }

})();