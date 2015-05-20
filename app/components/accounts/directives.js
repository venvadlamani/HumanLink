'use strict';

/**
 * Caregiver add license template.
 */
angular
    .module('Accounts')
    .directive('hlAddLicense', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_add_license.html'
        };
    });

/**
 * Caregiver add certification template.
 */
angular
    .module('Accounts')
    .directive('hlAddCertification', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_add_certification.html'
        };
    });
