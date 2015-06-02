'use strict';

(function () {
    angular
        .module('Search')
        .controller('SearchMainCtrl',['$scope', '$state', '$stateParams',function Ctrl($scope, $state, $stateParams) {
            // hide the search more filter block
            $scope.hide_filter = false;
            // category types
            $scope.category_types = ['Companion Care', 'Personal Care', 'Alzheimers and Dementia'];
            // Special skills
            $scope.special_skills = ['Hoyer Lift', 'Ambulation', 'Seizures', 'Catheter',
                                    'Hospice', 'COPD', 'SKin/wounds', 'Physical therapy',
                                    'Wheelchair accessible car', 'Prosthetics', 'Trachea', 'Transferring'];

            // Calender Settings
            $scope.today = function() {
                $scope.care_date = new Date();
            };
            $scope.today();

            $scope.clear = function () {
                $scope.care_date = null;
            };

            $scope.open = function($event) {
                $event.preventDefault();
                $event.stopPropagation();

                $scope.opened = true;
            };
            $scope.formats = ['MM/dd/yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
            $scope.format = $scope.formats[0];

            // Gender settings
            $scope.selected_gender = 'Male';
            $(".gender_panel ul.dropdown-menu li").on('click',function($event){
                $event.preventDefault();
                $scope.selected_gender = $(this).find('a').text(); // set selected gender val
            });

            // Filter button
            $scope.filter_val = 'More Filters';
            $scope.toggleFilter = function() {
                if($scope.filter_val == "More Filters"){
                    $scope.filter_val = "Hide Filters";
                    $scope.hide_filter = true;
                }else{
                    $scope.filter_val = "More Filters";
                    $scope.hide_filter = false;
                }
            }


        }]);

    /** @ngInject */
    function Ctrl($scope, $state, $stateParams) {
        $scope.title = 'Hello';
    }
})();
