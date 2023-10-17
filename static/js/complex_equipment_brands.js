let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [1] },
        { searchable: false, targets: [1]}
    ],
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listProgrammers();

    dataTable = $("#datatable-users").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listProgrammers = async () => {
    try {
        const response = await fetch("/configuracion/equipment/ajax/request/");
        const data = await response.json();

        let content = ``;
        data.brands.forEach((brands, index) => {
            content += `
                <tr>
                    <td>${brands.name}</td>
                    <td class='text-end'>
<a href="/configuracion/equipment/brands/edit/${brands.id}/" type="button" class="btn btn-primary">Edit</a>
<button type="button" onClick="delete_id(${brands.id})" data-id="${brands.id}" type="button" class="btn btn-danger eliminar-registro">Delete</button>
</td>
                </tr>`;
        });
        tableBody_users.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});

function delete_id(id) {
    $('#modal_user_delete').modal('show');
    $('#delete_id').val(id);
}
function confirm_delete() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    fetch(`/configuracion/equipment/brands/delete/${id}/`, {
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