$( document ).ready(function() {

});
$("input, select, option, textarea", "#equipment_form_edit").prop('disabled',true);
document.getElementById("save_b").style.visibility = "hidden";
$('#save_b').css({"display":"none"});

$("#edit_b").click(function(){
	$("input, select, option, textarea", "#equipment_form_edit").prop('disabled',false);
	$("#id").prop('disabled', true);
	$('#edit_b').css({"display":"none"});
    $('#save_b').css({"display":"block"});
    document.getElementById("save_b").style.visibility = "visible";
});
$("#save_b").click(function(){
    $("#equipment_form_edit").submit();
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
                })
                .catch(error => console.error('Error:', error));
    $('#modal_user_delete').modal('hide');
}
