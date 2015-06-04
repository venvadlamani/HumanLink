'use strict';

/**
 * SearchMainCtrl
 * @namespace Controllers
 */

(function () {
    angular
        .module('Search')
        .controller('SearchMainCtrl',Ctrl);
    /**
     * @namespace SearchMainCtrl
     * @desc Search caregivers
     * @memberOf Controllers
     */

    /** @ngInject */
    function Ctrl($scope,Constants, $state, $stateParams) {

        /* jshint validthis: true */
        var vm = this;
        /** toggle search filter block */
        vm.showFilterBlock = false;
        /** category types */
        vm.careServices = Constants.careServices;
        /** Special skills */
        vm.specialSkillServices = Constants.specialSkillServices;
        /** Languages */
        vm.languages = Constants.languages;
        /** Search Result */
        vm.caregiversSearchResult = [];

        /** Set default values
         * */
        vm.gender = 'Male';
        vm.liveIn = 'No';
        vm.language = vm.languages[0].name;

        vm.filterVal = 'More Filters';
        vm.showCaregiversCount = false;
        vm.showCaregiverHelp = false;
        vm.showCaregiverBlock = false;
        vm.showSkills = true;

        /** Calender Settings */
        vm.dateFormat = 'MM/dd/yyyy'; // set this format for the care date
        vm.gotoToday = gotoToday;
        gotoToday(); // set today date as default
        vm.toggleDatePicker = toggleDatePicker;

        //  buttons click functions
        vm.toggleFilterBlock = toggleFilterBlock;
        vm.getSearchResult = getSearchResult;

        vm.toggleSkillsBlock = toggleSkillsBlock;

            /**
         * @name gotoToday
         * @desc set current date
         * @returns {Void}
         */
        function gotoToday() {
            vm.careDate = new Date();
        }
        /**
         * @name toggleDatePicker
         * @desc toggle picker when click on the calender icon
         * @param {Object}
         * @returns {Void}
         */
        function toggleDatePicker($event) {
            $event.preventDefault();
            $event.stopPropagation();
            vm.opened = !vm.opened;
        }
        /**
         * @name toggleFilterBlock
         * @desc toggle filter button block when click on the filter button
         * @returns {Void}
         */
        function toggleFilterBlock() {
            if(vm.showFilterBlock)
               vm.filterVal = "More Filters";
            else
               vm.filterVal = "Hide Filters";

            vm.showFilterBlock = !vm.showFilterBlock;
        }
        /**
         * @name getSearchResult
         * @desc Get search static results array from global constants
         * @returns {Void}
         */
        function getSearchResult() {

            // API call goes here, using dummy data for now

            var data = tempCaregiversSearchResults;
           // var data = []; //uncomment this line to view no search results

            if(data.length){
                vm.caregiversSearchResult = tempCaregiversSearchResults;
                vm.showCaregiverHelp = false;
                vm.showCaregiverBlock = true;
            }
            else{
                vm.showCaregiverHelp = true;
                vm.showCaregiverBlock = false;
            }
            vm.showCaregiversCount = true;

        }

        function toggleSkillsBlock(){

            if(vm.showSkills)
                vm.toggleSkillsIcon = 'glyphicon-plus';
            else
                vm.toggleSkillsIcon = 'glyphicon-minus';

            vm.showSkills = !vm.showSkills;
        }

        // caregivers search temp results
        var tempCaregiversSearchResults = [
            {
                "name": "Ganesh Sundarapu",
                "description": "I am an awesome caregiver located at AKP",
                "hoursServiceCount": 30,
                "hoursAvgResTime": 1,
                "references": 8,
                "image": "/images/profile_ArianaA.png"
            },
            {
                "name": "Chalapathi Raju",
                "description": "I am an awesome caregiver located at VSKP",
                "hoursServiceCount": 20,
                "hoursAvgResTime": 2,
                "references": 20,
                "image": "/images/profile_ArianaA.png"
            }
        ];

    }
})();
