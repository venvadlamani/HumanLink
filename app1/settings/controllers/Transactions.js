(function () {
    'use strict';

    angular
        .module('app.settings')
        .controller('Transactions', Transactions);

    /* @ngInject */
    function Transactions($scope, $timeout, SettingsRepo,
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
