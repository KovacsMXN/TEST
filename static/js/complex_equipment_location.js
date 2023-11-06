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
let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [2] },
        { searchable: false, targets: [1]}
    ],
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listProgrammers();

    dataTable = $("#datatable-programmers").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listProgrammers = async () => {
    try {
        const response = await fetch("/configuracion/equipment/locations/ajax/request/");
        const data = await response.json();

        let content = ``;
        data.data_raw.forEach((data_raw, index) => {
            content += `
                <tr>
                    <td><span style="height: 18px;width: 18px;background-color: ${data_raw.color};border-radius: 0%;vertical-align: sub;display: inline-block;" class="dot"></span> ${data_raw.name}</td>
                    <td>${data_raw.equipment_count} records</td>
                    <td class="text-end"><a href="/configuracion/equipment/locations/edit/${data_raw.id}" class="btn btn-dark btn-sm">View</a> <button onclick="equipment_location_delete(${data_raw.id});" class="btn btn-danger btn-sm">Delete</button></td>
                </tr>
      </button>
    </h2>
</div>`;
        });
        tableBody_programmers.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});