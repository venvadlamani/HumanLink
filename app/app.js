window.is_backend_ready = false;

var getApiUrl = function() {
    var host = window.location.host;
    var protocol = host.indexOf('localhost') === 0 ? 'http://' : 'https://';
    return protocol + host + '/_ah/api';
};

function init() {
    if(window.HumanLink.modules) {
        gapi.client.load('humanlink', 'v1', function() {
            angular.bootstrap(document.body, window.HumanLink.modules);
        }, getApiUrl());
    }
}
