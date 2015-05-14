'use strict';

/**
 * A module that is common to all other site modules.
 */
angular
    .module('Common', [])
    .run(['$rootScope', '$location', 'userSession', function ($rootScope, $location, userSession) {

        // Listener that gets called when the state of the module changes.
        $rootScope.$on('$stateChangeStart', function (event, toState, toParams, fromState, fromParams) {
            // No need to update userSession on page load.
            if (!fromState.abstract) {
                userSession.update();
            }
        });

        // siteAlert is global.
        $rootScope.siteAlert = {};
    }])
    .config(['$compileProvider', function ($compileProvider) {
        if (HL.helpers.isProd()) {
            $compileProvider.debugInfoEnabled(false);
        }
    }])
    .controller('commonCtrl', ['$scope', function ($scope) {
        // Empty.
    }]);
