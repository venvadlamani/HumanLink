'use strict';

/**
 * Controller for caregiver profile page
 */
angular
    .module('Accounts')
    .controller('caregiverProfileCtrl', ['$scope', function ($scope) {
        $scope.caregiver = {
            name: 'First Last',
            phone: '(555)555-5555',
            rating: 4,
            background_verified: true,
            community_verified: true,
            badges: {
                care_hours: 2100,
                no_shows: 4,
                beacons_answered: 14
            },
            certifications: [
                'CNA (Schmeiding Center)',
                'Bentonville High School'
            ],
            connections: [
                'Si Robertson',
                'Wayne Hoyt',
                'Reynold Grover'
            ],
            complements: [
                {
                    name: 'Si Robertson',
                    description: 'Ariana is a wonderful...'
                }
            ]
        };

        $scope.owner = false;
    }]);
