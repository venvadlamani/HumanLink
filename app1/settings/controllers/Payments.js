(function () {
    'use strict';

    angular
        .module('app.settings')
        .controller('Payments', Payments);

    /* @ngInject */
    function Payments($scope, $timeout, SettingsRepo,
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
