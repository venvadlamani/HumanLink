'use strict';

angular
    .module('Accounts')
    .controller('settingsProfileCareseekerCtrl',
    ['$scope', '$anchorScroll', '$location', '$filter',
        'Constants', 'apiService', 'siteAlert',
    function ($scope, $anchorScroll, $location, $filter,
              Constants, apiService, siteAlert) {

        $scope.recipient = {};
        $scope.recipients = null;
        $scope.myself = false;
        $scope.forms = null;

        $scope.careServices = Constants.careServices;
        $scope.states = Constants.states;
        $scope.expertise = Constants.expertise;

        $scope.relationships = [
            'Myself',
            'Mother', 'Father',
            'Wife', 'Husband',
            'Grandmother', 'Grandfather',
            'Sister', 'Brother',
            'Other'
        ];

        $scope.chooseMyself = chooseMyself;
        $scope.save = save;
        $scope.edit = edit;
        $scope.archive = archive;
        $scope.toggleForm = toggleForm;

        init();

        var saveReq = new HL.CtrlHelper();
        var myselfOption = 'Myself';

        function init() {
            reset();
            var initReq = new HL.CtrlHelper();
            initReq.success = function (data, status) {
                $scope.recipients = data.items || [];
            };
            initReq.failure = function (data, status) {
                siteAlert.error(data);
            };
            apiService.Accounts.patients.list(initReq);
        }

       function chooseMyself(yes) {
            if (yes == $scope.myself) {
                return;
            }
            var first = '', last = '', phoneNumber = '', relationship = '';
            if (yes) {
                first = $scope.account.first;
                last = $scope.account.last;
                phoneNumber = $scope.account.phone_number;
                relationship = myselfOption;
            }
            $scope.myself = yes;
            $scope.recipient.first = first;
            $scope.recipient.last = last;
            $scope.recipient.phone_number = phoneNumber;
            $scope.recipient.relationship = relationship;
        }

        /**
         * Add a new care recipient.
         * @param model PatientApiModel.
         */
        function save(model) {
            siteAlert.clear();
            var ind = -1;
            // TODO: Move this outta here. Polyfill with es6-shim maybe.
            for (var i = 0; i < $scope.recipients.length; i++) {
                if (model.id === $scope.recipients[i].id) {
                    ind = i;
                    break;
                }
            }
            model = angular.copy(model);
            if (!validate(model)) {
                return;
            }
            saveReq.success = function (data, status) {
                siteAlert.success('Care recipient saved.');
                if (ind >= 0) {
                    $scope.recipients[i] = data;
                } else {
                    $scope.recipients.push(data);
                }
                reset();
            };
            saveReq.failure = function (data, status) {
                siteAlert.error('Uh-oh, there was a problem with your request.');
            };
            apiService.Accounts.patients.update(model, saveReq);
        }

        function edit(model) {
            siteAlert.clear();
            model = angular.copy(model);
            $scope.recipient = model;
            $scope.myself = model.relationship === myselfOption;
            $scope.forms.showNewCare = true;
            goToEdit();
        }

        function archive(model) {
            siteAlert.clear();
            if (!window.confirm("Are you sure?")) {
                return;
            }
            model.isLoading = true;
            var archiveReq = new HL.CtrlHelper();
            var ind = $scope.recipients.indexOf(model);
            $scope.recipients.splice(ind, 1);

            // Restore.
            archiveReq.failure = function (data, status) {
                siteAlert.error('Care recipient could not be archived.');
                model.isLoading = false;
                $scope.recipients.splice(ind, 0, model);
            };
            apiService.Accounts.patients.remove(model.id, archiveReq);
        }

        function toggleForm() {
            if ($scope.forms.showNewCare) {
                reset();
            } else {
                $scope.forms.showNewCare = true;
            }
        }

        var validate = function (model) {
            if (!model.care_type) {
                siteAlert.error("Please select the recipient's care needs.");
                return false;
            }
            if (!model.first || !model.last) {
                siteAlert.error("Please enter the care recipient's name.");
                return false;
            }
            if (!model.address) {
                siteAlert.error("Please enter the care recipient's address.");
                return false;
            }
            if (model.phone_number) {
                if (!HL.helpers.isValidPhone(model.phone_number)) {
                    siteAlert.error('Please enter a valid phone number.');
                    return false;
                }
                // Endpoint expects an integer.
                model.phone_number = model.phone_number.replace(/\D/g,'');
            } else {
                delete model.phone_number;
            }
            if (model.age && !/^\d+$/.test(model.age)) {
                siteAlert.error('Please enter a valid age.');
                return false;
            }
            return true;
        };

        function goToEdit () {
            $location.hash('new-care');
            $anchorScroll();
        }

        function reset() {
            $scope.recipient = {};
            $scope.myself = false;

            $scope.forms = {
                showNewCare: false,
                showShowExpertise: false,
                showMore: false
            };
        }
    }
    ]);