'use strict';

/**
 * Controller for the Edit Caregiver Profile subpage of settings
 */
angular
    .module('Accounts')
    .controller('settingsCaregiverCtrl', ['$scope', '$http', function ($scope, $http) {

        $scope.initData = {
            "schools":          ["Schmeiding Center", "NTI", "Blue Cliff"],
            "certifications":   ["Certified Nursing Assistant", "Licensed Practical Nurse", "Nursing Assistant",
                                "Home Health Aide", "Medical Assistant"],
            "years":            ["2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
                                "2011", "2012", "2013", "2014", "2015"],
            "months":            ["January", "February", "March", "April", "May", "June", "July",
                                "August", "September", "October", "November", "December"],
            "languages":        ["English", "Spanish", "German", "Vietnamese", "Filipino", "Hindi", "French",
                                "Swahili", "Bahasa", "Russian", "Polish", "Slavic"]
        };

        $scope.aboutMe = {
            "gender":"Male",
            "careservices": [{ "name":"BathingDressingGrooming", "value": false },
                             { "name":"Companionship", "value": false },
                             { "name":"EatingAssistance", "value": false },
                             { "name":"GastrointestinalCare", "value": false },
                             { "name":"LightHousekeeping", "value": true },
                             { "name":"MealPreparation", "value": true },
                             { "name":"MedicationManagement", "value": false },
                             { "name":"MobilityAssistance", "value": false },
                             { "name":"ToiletingAndIncontinence", "value": false },
                             { "name":"Transportation", "value": false },
                            ],
            "allergies":    [{ "name":"Cats", "value": false },
                             { "name":"Dogs", "value": true },
                             { "name":"Smoking", "value": true },
                            ],
            "genderPref":   'Women',
            "description":  "I am an awesome caregiver",
            "certifications":   [
                                { "school":"Schmeiding Center", "title": "Certified Nursing Aide",
                                "year": "2012", "month": "January" }
                                ],
            "emergencys":   [{ "name":"Joe Smith", "phone": "479-555-1212" }],
            "languages":    [{ "language":"English" },
                            ]
        };

        /*
         * isEven is a function to keep track of "Add <data>"  state of inputs
         */
        $scope.isEven = function(value){
            if(value % 2 === 0)
                return true;
            else
                return false;
        }

        /*
         * Add/Delete functions for certifications, languages and emergency contacts
         */
        $scope.addCert = 1;
        $scope.addCertification = function(index) {
            $scope.aboutMe.certifications.push({
                    "school": $scope.certification.school,
                    "title": $scope.certification.title,
                    "year": $scope.certification.year,
                    "month": $scope.certification.month
            });
            $scope.addCert = $scope.addCert + 1;
            $scope.certification = "";
          };
        $scope.deleteCertification = function(index) {
            $scope.aboutMe.certifications.splice(index,1);
        };

        $scope.addEmer = 1;
        $scope.addEmergency = function(index) {
            $scope.aboutMe.emergencys.push({ "name" : $scope.emergency.newName, "phone": $scope.emergency.newNumber });
            $scope.addEmer = $scope.addEmer + 1;
            $scope.emergency = "";
        };
        $scope.deleteEmergency = function(index) {
            $scope.aboutMe.emergencys.splice(index,1);
        };

        $scope.addLang=1;
        $scope.addLanguage = function(index) {
            $scope.aboutMe.languages.push({"language": $scope.newLanguage });
            $scope.addLang = $scope.addLang + 1;
            $scope.newLanguage = "";
        };
        $scope.deleteLanguage = function(index) {
            $scope.aboutMe.languages.splice(index,1);
        };

        /*
         * Save "About Me" and "Additional Infomation" data
         */
        $scope.submitAboutMe = function(aboutMe){
            console.log(aboutMe);
        }

    }]);
