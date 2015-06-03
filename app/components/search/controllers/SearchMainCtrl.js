'use strict';

(function () {
    angular
        .module('Search')
        .controller('SearchMainCtrl',Ctrl);

    /** @ngInject */
    function Ctrl($scope,Constants, $state, $stateParams) {
        /** toggle search filter block */
        $scope.hideFilter = false;
        /** category types */
        $scope.careServices = Constants.careServices;
        /** Special skills */
        $scope.specialSkillServices = Constants.specialSkillServices;
        /** Languages */
        $scope.languages = Constants.languages;
        /** Set first position lang */
        $scope.selectedLang = $scope.languages[0].name;
        /** Search Result */
        $scope.caregiversSearchRes = [];
        /** Hide Caregivers count */
        $scope.showCaregiversCount = false;

        /** Calender Settings */
        $scope.today = function() {
            $scope.careDate = new Date();
        };
        $scope.today();

        $scope.clear = function () {
            $scope.careDate = null;
        };

        $scope.open = function($event) {
            $event.preventDefault();
            $event.stopPropagation();

            $scope.opened = true;
        };
        /** set calender date format */
        $scope.format = 'MM/dd/yyyy';

        /** Gender settings */
        $scope.selectedGender = 'Male';
        $scope.selectedLiveIn = 'No';

        /** Filter button */
        $scope.filter_val = 'More Filters';
        $scope.toggleFilter = function() {
            if($scope.filter_val == "More Filters"){
                $scope.filter_val = "Hide Filters";
                $scope.hideFilter = true;
            }else{
                $scope.filter_val = "More Filters";
                $scope.hideFilter = false;
            }
        }

        /** search page response */
       $scope.searchFilter = function(){
           $scope.showCaregiversCount = true;
           $scope.caregiversSearchRes = Constants.caregiversSearchRes;
       };



    }
})();
