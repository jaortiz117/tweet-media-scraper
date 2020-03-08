$(document).ready(function(){
  $('#search-btn').click( function() {
    data = {term:$('input#search.form-control').val()}
    console.log(data)
    $.ajax({
        url: 'download',
        type: 'GET',
        contentType: 'application/json; charset=UTF-8',
        data: data,
        // data: JSON.stringify(data),
        processData: false,
        beforeSend: function(){
          $("#loader").show();
        },
        success: function(data) {
          $("#loader").hide();
        }
    });
});
});
