let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [1,2] },
        { searchable: false, targets: [1,2] }
    ],
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listProgrammers();

    dataTable = $("#datatable-storage-locations").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listProgrammers = async () => {
    try {
        const response = await fetch("/configuracion/storage/ajax/request/");
        const data = await response.json();

        let content = ``;
        data.storage_location.forEach((storage_location, index) => {
            content += `
                <tr>
                    <td>${storage_location.name}</></td>
                    <td>${storage_location.add_date}</></td>
                    <td class='text-end'><a type="button" href="/configuracion/storage/edit/${storage_location.id}/" class="btn btn-dark">View</a> <button onClick="modal_storage_location_delete(${storage_location.id})" type="button" class="btn btn-danger">Delete</button></td>
                </tr>`;
        });
        tableBody_storage_locations.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});

function modal_storage_location_delete(id) {
    $('#modal_storage_location_delete').modal('show');
    $('#delete_id').val(id);
}

function confirm_delete_storage_location_delete() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    fetch(`/configuracion/storage/ajax/delete/${id}/`, {
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