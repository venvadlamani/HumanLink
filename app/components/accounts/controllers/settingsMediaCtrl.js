'use strict';

/**
 * Controller for the media subpage of settings
 */
angular
    .module('Accounts')
    .controller('settingsMediaCtrl', ['$scope', '$http', 'fileUpload', 'userSession',
        function ($scope, $http, fileUpload, userSession) {

            $scope.mediaCollection = {};
            $scope.usr = userSession;
            var account_id = $scope.usr.userdata.account_id;
            var uploadUrl = '/post_image';

            function init() {
            }
            init();

            $scope.uploadFile = function () {
                var file = $scope.myFile;
                fileUpload.uploadFileToUrl(file, uploadUrl, account_id);
            };

            $scope.getFile = function () {
                $http({
                    url: '/get_images',
                    method: "GET",
                    params: {account_id: account_id}
                }).then(function (response) {
                    $scope.mediaCollection = response.data;
                }, function (response) {
                    $scope.siteAlert.type = "danger";
                    $scope.siteAlert.message = ("Oops. " + response.status + " Error. Please try again.");
                });

            }

        }]);
