$(function() {
    $('#btnSearch').click(function() {
 
        $.ajax({
            url: '/autocomplete',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                // console.log(response);
                $( ".test" ).append( "Test" );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(function() {
    $('#search').keypress(function() {
 
        $.ajax({
            url: '/autocomplete',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                // console.log(response);
                $( ".test" ).append( response );
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});