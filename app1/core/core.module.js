/**
 * Core module that bootstrap most of the dependencies and configuration.
 */
(function () {
    'use strict';

    angular
        .module('app.core', [
            'ngAnimate',
            'ui.router',
            'ui.bootstrap',

            'app.common'
        ])
        .config(Config);

    /** ngInject */
    function Config($compileProvider) {
        if (HL.helpers.isProd) {
            $compileProvider.debugInfoEnabled(false);
        }
    }

})();
