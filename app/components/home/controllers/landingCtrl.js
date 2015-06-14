'use strict';

/**
 * Main landing page.
 */
(function () {
    angular
        .module('Home')
        .controller('LandingCtrl', Ctrl);

    /** @ngInject */
    function Ctrl($scope, $http, $location, $anchorScroll) {
        $scope.price = 12;
        $scope.showInvite = true;
        $scope.invite = invite;
        $scope.gotoInvite = gotoInvite;
        $scope.$watch('pricing', priceWatch, true);
        $scope.pricing = {
            services: [0],
            shortHours: '',
            zipcode: ''
        };
        $scope.contact = {
            interest: 2
        };

        function priceWatch(newValue, oldValue) {
            updatePrice(newValue);
        }

        function updatePrice(pricing) {
            var price = 12;
            angular.forEach(pricing.services, function (value, key) {
                price += value;
            });
            if (pricing.shortHours) {
                price += 2;
            }
            $scope.price = price;
        }

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
                })
                .error(function () {
                    // Dang.
                });
        }
    }

})();