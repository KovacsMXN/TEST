$( document ).ready(function() {

});
$("input, select, option, textarea", "#equipment_form_edit").prop('disabled',true);
document.getElementById("submit_b").style.visibility = "hidden";

$("#edit_b").click(function(){
	$("input, select, option, textarea", "#equipment_form_edit").prop('disabled',false);
	$("#id").prop('disabled', true);
	document.getElementById("edit_b").style.visibility = "hidden";
	document.getElementById("submit_b").style.visibility = "visible";
});

function delete_image(id) {
	$('#delete_image_Modal').modal('show');
	$('#delete_id').val(id);
}
function confirm_delete_image() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    fetch(`/equipment/imagen/delete/${id}/`, {
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