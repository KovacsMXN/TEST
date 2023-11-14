$("input, select, option, textarea", "#forklift_form_edit").prop('disabled',true);
document.getElementById("save_b").style.visibility = "hidden";
$('#save_b').css({"display":"none"});

$("#edit_b").click(function(){
    $("input, select, option, textarea", "#forklift_form_edit").prop('disabled',false);
    $("#id").prop('disabled', true);
    $('#edit_b').css({"display":"none"});
    $('#save_b').css({"display":"block"});
    document.getElementById("save_b").style.visibility = "visible";
});
$("#save_b").click(function(){
    $("#forklift_form_edit").submit();
});
function delete_forklift(id) {
    $('#modal_delete_forklift').modal('show');
    $('#delete_id').val(id);
};

function confirm_delete_forklift() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    fetch(`/forklifts/json/delete/forklifts/${id}`, {
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