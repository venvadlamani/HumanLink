'use strict';
/**
 * Caregiver professional credentials template.
 */
angular
    .module('Accounts')
    .directive('hlProfessionalCredentials', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_professional_credentials.html'
        };
    });

/**
 * Caregiver Status and Description template.
 */
angular
    .module('Accounts')
    .directive('hlDescriptionStatus', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_description_status.html'
        };
    });

/**
 * Caregiver professional preferences template.
 */
angular
    .module('Accounts')
    .directive('hlProfessionalPreferences', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_professional_preferences.html'
        };
    });

/**
 * Caregiver skills template.
 */
angular
    .module('Accounts')
    .directive('hlSkills', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_skills.html'
        };
    });

/**
 * Caregiver additional information template.
 */
angular
    .module('Accounts')
    .directive('hlAdditionalInformation', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_additional_information.html'
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
 * Caregiver add experience template.
 */
angular
    .module('Accounts')
    .directive('hlAddExperience', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_add_experience.html'
        };
    });

/**
 * Caregiver add emergency template.
 */
angular
    .module('Accounts')
    .directive('hlAddEmergency', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_add_emergency.html'
        };
    });

/**
 * Caregiver add languages template.
 */
angular
    .module('Accounts')
    .directive('hlAddLanguage', function () {
        return {
            restrict: 'E',
            templateUrl: '/views/accounts/partials/dir/caregiver_add_language.html'
        };
    });

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
