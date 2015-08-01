'use strict';

angular
    .module('Accounts')
    .controller('settingsRecipientsCtrl',
    ['$scope', '$anchorScroll', '$location', '$filter',
        'Constants', 'apiService', 'siteAlert',
        function ($scope, $anchorScroll, $location, $filter,
                  Constants, apiService, siteAlert) {

            $scope.recipient = {};
            $scope.recipients = null;


        }
    ]);