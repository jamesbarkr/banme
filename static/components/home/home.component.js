angular.
module('homeApp').
component('home',{
	templateUrl:
	'/static/views/home.html',
	controller:['$scope','$http',function($scope,$http){
		$scope.post="";
		function setData(data){
			$scope.post=data;
		};
		var getPost=function(callback){
			setTimeout( callback("Donald Trump adds pineapple to pizza!"), 500);
		};

		getPost(setData);

		console.log($scope);
	}]
});