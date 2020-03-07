$(document).ready(function(){
  $('#search-btn').click( function() {
    console.log({term: $('input#search.form-control').val()})
    $.ajax({
        url: 'download',
        type: 'get',
        dataType: 'application/json',
        data: {term: $('input#search.form-control').val()},
        beforeSend: function(){
          $("#loader").show();
        },
        success: function(data) {
          $("#loader").hide();
        }
    });
});
});
