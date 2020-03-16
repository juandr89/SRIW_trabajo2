$('#idC').on('input', function() {
    $.ajax({
        type: 'GET',
        url: '/parqueaderos/buscar-cliente/' + String($(this).val()) + '/',
        success: (data) => {
            $('#nameC').val(data.name)
            $('#lastnameC').val(data.lastname)
        }
    })
})