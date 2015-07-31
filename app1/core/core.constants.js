(function () {
    'use strict';

    angular
        .module('app.core')
        .constant('Constants', window.HL.constants)
        .constant('Helpers', window.HL.helpers)
        .constant('Config', getConfig());

    function getConfig() {
        return {
            api_path: '/api'
        };
    }

})();
