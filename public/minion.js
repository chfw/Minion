function runit() {
	$.ajax({
		url: '/api/run/',
		method: 'POST',
		dataType: 'json',
		data: JSON.stringify({ 'command': $('#command').val() }),
		contentType: "application/json; charset=utf-8",
		success: function(data){
			$('#result').html(data['result']);
			show_result();
		},
		error: function(xhr){
			$('#result').html("error message:" + xhr.responseJSON['message']);
			show_result();
		}
	})
};


function hide_result(){
	$('#result').css('display', 'None');
}

function show_result(){
	$('#result').hide().fadeIn('slow');
}
