angular.
  module('banMeApp').
  config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/', {
          template: '<home></home>'
        }).
        when('/devs', {
          template: '<devs></devs>'
        }).
        otherwise('/');
    }
  ]);