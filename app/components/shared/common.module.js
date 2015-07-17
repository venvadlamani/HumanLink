'use strict';

/**
 * A module that is common to all other site modules.
 */
angular
    .module('Common', [])
    .run(['$rootScope', '$location', 'userSession', '$state', '$window', '$timeout',
        function($rootScope, $location, userSession, $state, $window, $timeout) {

            // Listener that gets called when the state of the module changes.
            $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams) {
                // No need to update userSession on page load.
                if (!fromState.abstract) {
                    userSession.update();
                }
                var requiredLogin = toState.data.requireLogin;
                var redirectLogin = '';
                // no log in for required log in
                if ((!userSession.isAuthorized()) && requiredLogin) {
                    //alert();
                    event.preventDefault();
                    redirectLogin = $state.href('login.page', {
                        page: toState.name
                    });
                    $window.location.href = redirectLogin;
                    $timeout(function() {
                        $window.location.reload();
                    }, 0);
                }

                if (userSession.isAuthorized() && (!requiredLogin)) {
                    event.preventDefault();

                    var redirectUrl = $location.path().split('/');
                    var redirectPage = '';
                    if (typeof redirectUrl[2] != 'undefined') {
                        redirectPage = redirectUrl[2];
                    }
                    console.log(redirectPage);
                    if (redirectPage == '') {
                        $state.go('profile', {}, {
                            reload: true
                        });
                    } else {
                        $state.go(redirectPage, {}, {
                            reload: true
                        });
                    }
                }
            });

            // siteAlert is global.
            $rootScope.siteAlert = {};
        }
    ])
    .config(['$compileProvider', function($compileProvider) {
        if (HL.helpers.isProd()) {
            $compileProvider.debugInfoEnabled(false);
        }
    }])
    .controller('commonCtrl', ['$scope', function($scope) {
        // Empty.
    }]);