console.log('Loaded admin.js');

//ADMIN-BLOG PAGE handlers


//ADMIN-CONTACT_US handlers



//ADMIN-CAREERS handlers 

// ADMIN-MAIN PAGE

function handleGetClick(){ 	
	$.ajax ( '/ctadmin', 
			{
				type: 'GET',
				data: {
					'fmt' : 'json' 
					},
				dataType: 'json',
				success: function (data) {
				    //Query the jQuery object for the values
					$("#name").val (data.name);
					$("#age").val (data.age);
					}
			}
			) ;
}

var jsData = {
	    id:         'E1',
	    firstname:  'Peter',
	    lastname:   'Funny',
	    project: { id: 'P1' },
	    activities: [
	        { id: 'A1' },
	        { id: 'A2' }
	    ]};

var jsonData = JSON.stringify(jsData);

function handlePostClick(){
    $.ajax({
        url: '/ctadmin',
        type: 'POST',
        data: jsonData,
        dataType: 'json',
        success: function (data){
        console.log(data);
        },
        error:function(){$('#text').html('FATAL_ERROR')}

    })
}

$(document).ready(function(){	
								$('#getitbutton').on('click', handleGetClick)	
								$('#postitbutton').on('click', handlePostClick)
								
								
							}
				 );