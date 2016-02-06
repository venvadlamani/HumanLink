'use strict';

angular
    .module('Accounts')
    .controller('settingsProfileCaregiverCtrl', ['$scope', 'Constants', 'apiService', 'userSession',
        function ($scope, Constants, apiService, userSession) {
            var updateReq = new HL.CtrlHelper();
            var userdata = userSession.userdata;

            $scope.aboutMe = {};

            $scope.aboutMe.certifications = [];
            $scope.certifications = {};

            $scope.addCert = true;
            $scope.addExper = true;
            $scope.addLang = true;
            $scope.addLang = true;
            $scope.addEmer = true;

            $scope.allergies = Constants.allergies;
            $scope.vaccines = Constants.vaccines;
            $scope.careServices = Constants.careServices;
            $scope.expertise = Constants.expertise;
            $scope.languages = Constants.languages;
            $scope.transportation = Constants.transportation;
            $scope.states = Constants.states;
            $scope.certificates = Constants.certificates;

            $scope.caregiver = null;


            var init = function () {
                updateReq.success = function (data, status) {
                    fetch(data, status);
                };
                apiService.Accounts.caregiver.get(userdata.account_id, updateReq);
            };
            init();

            $scope.caregiverUpdate = function (model) {
                if (!validate(model)) {
                    return;
                }
                // Maybe nothing has been changed.
                if (angular.equals($scope.caregiver, model)) {
                    return;
                }
                if (model.year) {
                    model.dob = new Date(model.year, 0);
                }
                updateReq.success = function (data, status) {
                    fetch(data, status);
                    $scope.siteAlert.type = "success";
                    $scope.siteAlert.message = "Changes have been saved.";
                };
                updateReq.failure = function (data, status) {
                    $scope.siteAlert.type = "danger";
                    $scope.siteAlert.message = "Uh-oh, there was a problem.";
                };
                apiService.Accounts.caregiver.update(model, updateReq);
            };

            var fetch = function (data, success) {
                if (data.dob) {
                    data.year = new Date(data.dob).getFullYear();
                }
                console.log(data);
                $scope.aboutMe = data;
            };

            var validate = function (model) {
                if (model.year && (model.year < 1900 ||
                    model.year > new Date().getFullYear() - 10)) {
                    return false;
                }
                return true;
            };

            //Maintain care services
            $scope.toggleSelection = function toggleSelection(careService) {
                console.log(careService);
                if ($scope.aboutMe.careServicesSelection) {
                    var idx = $scope.aboutMe.careServicesSelection.indexOf(careService);

                    // is currently selected
                    if (idx > -1) {
                        $scope.aboutMe.careServicesSelection.splice(idx, 1);
                    }

                    // is newly selected
                    else {
                        $scope.aboutMe.careServicesSelection.push(careService);
                    }
                }
            };

            //  Add/Edit certifications
            $scope.addCertification = function (certification) {
                if (!$scope.aboutMe.certifications) {
                    $scope.aboutMe.certifications = [];
                }
                $scope.aboutMe.certifications.push(certification);

                // Clear input fields after push
                $scope.addCert = true;
                $scope.certification = "";
            };

            //  Add/Edit experiences
            $scope.addCertification = function (exper) {
                if (!$scope.aboutMe.experiences) {
                    $scope.aboutMe.experiences = [];
                }
                $scope.aboutMe.experiences.push(exper);

                // Clear input fields after push
                $scope.addExper = true;
                $scope.experience = "";
            };

            //  Add/Edit languages
            $scope.addLanguage = function (language) {
                if (!$scope.aboutMe.languages) {
                    $scope.aboutMe.languages = [];
                }
                $scope.aboutMe.languages.push(language);

                // Clear input fields after push
                $scope.addLang = true;
                $scope.language = "";
            };

            $scope.deleteLanguage = function (index) {
                console.log("deleting " + index);
                _.without($scope.aboutMe.languages, index);
                console.log($scope.aboutMe.certifications);
            };
        }]);