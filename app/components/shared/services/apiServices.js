angular
    .module("Common")

    .factory("apiService", [function () {

        var apiService = {};

        apiService.getProfileInfo = function (profile_id, callback) {
            var params = {
                id: profile_id,
            };

            gapi.client.humanlink.accounts.profile.get(params)
            .execute(function (resp) {
                callback(resp);
            });
        };

        return apiService;
    }]);

