'use strict';

angular
    .module('Accounts')
    .controller('settingsProfileCtrl', ['$scope', function ($scope) {

        $scope.account = {
            careReceivers: [
                {
                    name: 'John Doe',
                    email: 'john@gmail.com',
                    allergies: []
                },
                {
                    name: 'Jane Doe',
                    allergies: ['Peanuts', 'Dogs']
                }
            ]
        };

        $scope.states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC',
        'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
        'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
        'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'];

        $scope.addAllergy = function (careReceiver) {
            careReceiver.allergies.push('');
        };

        $scope.addCareReceiver = function () {
            $scope.account.careReceivers.push({ name: 'New Care Receiver' });
        };

    }]);
