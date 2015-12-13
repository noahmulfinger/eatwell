$(function(){
	$('#btnSearch').click(function(){
		
		$.ajax({
			url: '/autocomplete',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$(".test").append(response);
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});