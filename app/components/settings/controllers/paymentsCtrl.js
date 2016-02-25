'use strict';

/**
 * Payments controller
 */
angular
    .module('Settings')
    .controller('paymentsCtrl', ['$scope', '$http', 'userSession', 'stripe',
        function ($scope, $http, userSession, stripe) {

            $scope.paymentModel = {};
            $scope.usr = userSession;
            var account_id = $scope.usr.userdata.account_id;

            var init = function () {

            };
            init();

            $scope.updatePayments = function (model) {
                return stripe.card.createToken(model.card_number)
                    .then(function (response) {
                        console.log('token created for card ending in ', response.card.last4);
                        var payment = angular.copy($scope.payment);
                        payment.card = void 0;
                        payment.token = response.id;
                        return $http.post('https://yourserver.com/payments', payment);
                    })
                    .then(function (payment) {
                        console.log('successfully submitted payment for $', payment.amount);
                    })
                    .catch(function (err) {
                        if (err.type && /^Stripe/.test(err.type)) {
                            console.log('Stripe error: ', err.message);
                        }
                        else {
                            console.log('Other error occurred, possibly with your API', err.message);
                        }
                    });
            };

        }]);
