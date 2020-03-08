$(document).ready(function(){
//   $('#search-btn').click( function() {
//     $("#loader").show();
//     term = $('input#search.form-control').val()
//     data = {term:term}
//     console.log(data)
//     $.ajax({
//         url: 'download',
//         type: 'POST',
//         contentType: 'application/json; charset=UTF-8',
//         // data: data,
//         data: JSON.stringify(data),
//         processData: false,
//         // beforeSend: function(){
//         //   $("#loader").show();
//         // },
//         success: function(data) {
//           // console.log(data)
//           $("#loader").hide();
//         }
//     });
// });
$('#search-form').submit(function() {
    $("#loader").show();
});
});
