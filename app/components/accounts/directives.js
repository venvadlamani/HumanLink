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


/**
 * Careseeker add care recipient.
 */
angular
    .module('Accounts')
    .directive('hlNewRecipient', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/careseeker_new_recipient.html'
        };
    });
