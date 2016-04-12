$(document).on('submit','#tweet_form',function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url : '/tweets/tweets_list/tweets_print/',
        data: {
            'name' : $('#name').val(),
            'count' : $('#count').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(json){
                $('#tweets_found').html(json.message);
                alert("Done");
        }
    });
})
