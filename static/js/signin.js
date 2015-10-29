$(function() {
    $('#btnSignIn').click(function() {
 
        $.ajax({
            url: '/dosignin',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});