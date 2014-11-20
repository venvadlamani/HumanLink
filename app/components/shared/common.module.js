'use strict';

/**
 * A module that is common to all other site modules.
 */
angular
    .module('Common', [])

    .run(['$rootScope', '$location', 'userSession', function($rootScope, $location, userSession) {

        // Listener that gets called when the state of the module changes.
        $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams) {
            userSession.update();
            // The above call is async so the following logic works with an outdated data.
            // We don't wait for the above call to finish because it is a bad UX.
            if (!userSession.isAuthorized()) {
                console.log('User not authorized.');
            }
        });

    }]);
