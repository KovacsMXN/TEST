function equipment_location_delete(id) {
    $('#modal_delete').modal('show');
    $('#delete_id').val(id);
}
function confirm_location_delete() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    fetch(`/configuracion/equipment/locations/delete/${id}/`, {
    method: 'POST',
    headers: {
    'X-CSRFToken': csrf,  // Asegúrate de tener la variable csrftoken definida
    },
                })
                .then(response => response.json())
                .then(data => {
                    //alert(data.mensaje);
                    // Puedes realizar alguna acción adicional después de la eliminación
                    // como recargar la página o actualizar la lista de registros
                })
                .catch(error => console.error('Error:', error));
    $('#modal_user_delete').modal('hide');
}