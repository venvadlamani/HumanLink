'use strict';

/**
 * Set focus on the element.
 * Example:
 *   <input type="text" hl-focus />
 */
angular
    .module('Common')
    .directive('hlFocus', function () {
        return {
            link: function (scope, element) {
                element[0].focus();
            }
        };
    });

/**
 * Attaches some data to the current scope.
 * Example:
 *   <hl-preload hl-key="foo" hl-value='{"a": "z", "b": [1, 2]}'></<hl-preload>
 *   will result in the current $scope to have a "foo" property with the
 *   given JSON value in hl-value.
 */
angular
    .module('Common')
    .directive('hlPreload', function () {
        return {
            restrict: 'E',
            link: function (scope, element, attrs) {
                scope[attrs.hlKey] = JSON.parse(attrs.hlValue);
                element.remove();
            }
        };
    });
