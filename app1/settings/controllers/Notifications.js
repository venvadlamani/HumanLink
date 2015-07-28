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
            // Timeout is only for demonstrating the loader.
            var timer = $timeout(load, 1500);
            onDestroy(timer);
        }

        function load() {
            SettingsRepo.getSettings().then(function(data) {
                CommonService.broadcast(CommonEvents.viewReady);
                vm.settings = data;
            });
        }

        function onDestroy(timer) {
            $scope.$on('$destroy', function () {
                $timeout.cancel(timer);
            });
        }
    }

})();
