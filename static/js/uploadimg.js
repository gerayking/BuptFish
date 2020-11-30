$.ajax({
    type : 'post',
    url : 'https://sm.ms/api/v2/upload',
    data: new FormData($('#avatar')[0]),
    contentType : false,
    success: function (data){},
})