'use strict';

/**
 * Interest controller
 */
(function () {
    angular
        .module('Home')
        .controller('interestCtrl', Ctrl);

    /** @ngInject */
    function Ctrl($scope, $http, $location, $anchorScroll) {
        $scope.showInvite = true;
        $scope.invite = invite;
        $scope.gotoInvite = gotoInvite;
        $scope.contact = {
            interest: $location.absUrl().indexOf('/caregiver') >= 0 ? 1 : 2
        };

        function gotoInvite() {
            $location.path('/');
            $location.hash('invite');
            $anchorScroll();
        }

        function invite(contact) {
            if (!contact.name || !contact.email || !contact.zipcode || !contact.interest) {
                return;
            }
            $http.post('/submit_contact', contact)
                .success(function (data, status) {
                    $scope.showInvite = false;
                    gotoInvite();
                })
                .error(function () {
                    // Dang.
                });
        }
    }

})();
