'use strict';

window.HL = window.HL || {};

window.HL.helpers = {
    /**
     * Returns whether or not the host is in production.
     */
    isProd: function () {
        var h = window.location.host;
        return (h.indexOf('humanlink.co') === 0 ||
                h.indexOf('care-tiger.appspot.com') === 0);
    }

};
