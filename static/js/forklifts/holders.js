function delete_forkliftowner(id) {
    $('#modal_delete').modal('show');
    $('#delete_id').val(id);
};

function confirm_delete_forkliftowner() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    fetch(`/forklifts/json/delete/forkliftsowners/${id}`, {
    method: 'POST',
    headers: {
    'X-CSRFToken': csrf,  // AsegÃºrate de tener la variable csrftoken definida
    },
                })
                .then(response => response.json())
                .then(data => {
                    //alert(data.mensaje);
                    // Puedes realizar alguna acciÃ³n adicional despuÃ©s de la eliminaciÃ³n
                    // como recargar la pÃ¡gina o actualizar la lista de registros
                })
                .catch(error => console.error('Error:', error));
    $('#modal_delete_forklift').modal('hide');
};