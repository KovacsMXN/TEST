function delete_content(id) {
    $('#modal_delete').modal('show');
    $('#delete_id').val(id);
};

function confirm_delete_content() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();

    // Realiza una solicitud AJAX utilizando jQuery
    $.ajax({
        type: 'POST',
        url: `/equipment/manufacturers/delete/${id}/`,
        data: {
            csrfmiddlewaretoken: csrf
        },
        success: function (data) {
            if (data.success) {
                // Redirige a la URL especificada en la respuesta JSON
                window.location.href = data.redirect_url;
            } else {
                // Maneja errores si es necesario
                console.log('Error al eliminar el registro');
            }
        },
        error: function () {
            // Maneja errores de conexión si es necesario
            console.log('Error de conexión al eliminar el registro');
        },
        complete: function () {
            // Oculta el modal después de procesar la solicitud
            $('#modal_delete').modal('hide');
        }
    });
}
