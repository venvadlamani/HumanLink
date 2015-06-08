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
    function Ctrl($scope,Constants) {

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

        // search form object
        vm.search = {
            languages: [],
            careServices: [],
            skillsServices: [],
            gender: 'Male',
            liveIn: 'No'
        };
        // submit the search form
        vm.searchCaregivers = searchCaregivers;

        vm.filterVal = 'More Filters';
        vm.showCaregiversCount = false;
        vm.showCaregiverHelp = false;
        vm.showCaregiverBlock = false;
        vm.showSkills = true;
        vm.showLanguage = true;

        /** Calender Settings */
        vm.dateFormat = 'MM/dd/yyyy'; // set this format for the care date
        vm.gotoToday = gotoToday;
        gotoToday(); // set today date as default
        vm.toggleDatePicker = toggleDatePicker;


        vm.toggleFilterBlock = toggleFilterBlock;
        vm.toggleSkillsBlock = toggleSkillsBlock;
        vm.toggleLanguageBlock = toggleLanguageBlock;

        // setters
        vm.setGender = setGender;
        vm.setLiveIn = setLiveIn;

        //  selected skills names string
        vm.selectedSkills = "";
        vm.getSelectedSkills = getSelectedSkills;

        // selected languages names string
        vm.selectedLanguages = "";
        vm.getSelectedLanguages = getSelectedLanguages;

        /**
         * @name searchCaregivers
         * @desc get caregivers for the input search  object
         * @returns {Void}
         */
        function searchCaregivers(search){
            // see log report in browser console for form search object
            // we are not perform form validation now
            console.log('form submit =  '+JSON.stringify(search));
            // get temp response object
            getSearchResult();
        }
        /**
         * @name gotoToday
         * @desc set current date
         * @returns {Void}
         */
        function gotoToday() {
            vm.search.careDate = new Date();
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
            if (vm.showFilterBlock) {
                vm.filterVal = "More Filters";
            }
            else {
                vm.filterVal = "Hide Filters";
            }

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

        /**
         * @name toggleSkillsBlock
         * @desc toggle the skills block
         * @returns {Void} */
        function toggleSkillsBlock(){

            if(vm.showSkills) {
                vm.toggleSkillsIcon = 'glyphicon-plus';
            }
            else {
                vm.toggleSkillsIcon = 'glyphicon-minus';
            }

            vm.showSkills = !vm.showSkills;

        }

        /**
         * @name toggleLanguageBlock
         * @desc toggle the language block
         * @returns {Void} */
        function toggleLanguageBlock(){

            if(vm.showLanguage) {
                vm.toggleLanguageIcon = 'glyphicon-plus';
            }
            else {
                vm.toggleLanguageIcon = 'glyphicon-minus';
            }

            vm.showLanguage = !vm.showLanguage;

        }

        /**
         * @name getSelectedSkills
         * @desc get selected skill names string
         * @returns {Void} */
        function getSelectedSkills() {
            vm.selectedSkills = vm.search.skillsServices.map(
                function(skill) { return skill.name; }
            );
        }

        /**
         * @name getSelectedSkills
         * @desc get selected skill names string
         * @returns {Void} */
        function getSelectedLanguages() {
            vm.selectedLanguages = vm.search.languages.map(
                function(lang) { return lang.name; }
            );
        }

        /**
         * @name setGender
         * @desc set gender for gender dropdown
         * @returns {Void} */
        function setGender(name){
            vm.search.gender = name;
        }

        /**
         * @name setLiveIn
         * @desc set live for live in dropdown
         * @returns {Void} */
        function setLiveIn(name){
            vm.search.liveIn = name;
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
