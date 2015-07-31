(function () {
    'use strict';

    angular
        .module('app.settings')
        .controller('Notifications', Notifications);

    /* @ngInject */
    function Notifications($scope, $timeout, SettingsRepo,
                           CommonService, CommonEvents) {
        var vm = this;
        vm.settings = null;

        init();

        function init() {
            load();
        }

        function load() {
            SettingsRepo.getSettings().then(function (data) {
                CommonService.broadcast(CommonEvents.viewReady);
                vm.settings = data;
            });
        }

    }

})();
