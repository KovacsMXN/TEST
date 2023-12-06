let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [3, 4, 5, 6] },
        { searchable: false, targets: [3, 4, 5, 6]}
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
        const response = await fetch("/staff/json/pull/");
        const data = await response.json();

        let content = ``;
        data.usuarios.forEach((usuarios, index) => {
            content += `
                <tr>
                    <td>${usuarios.first_name}</td>
                    <td>${usuarios.last_name}</td>
                    <td>${usuarios.username}</td>
                    <td>${usuarios.is_active >= true 
                        ? "<img class='filter-green' src='/static/images/ico/check-circle.svg'>" 
                        : "<img class='filter-red' src='/static/images/ico/x-circle.svg'>"}
                    </td>
                    <td>${usuarios.is_staff >= true 
                        ? "<img class='filter-green' src='/static/images/ico/check-circle.svg'>" 
                        : "<img class='filter-red' src='/static/images/ico/x-circle.svg'>"}
                    </td>
                    <td>${usuarios.is_superuser>= true 
                        ? "<img class='filter-green' src='/static/images/ico/check-circle.svg'>" 
                        : "<img class='filter-red' src='/static/images/ico/x-circle.svg'>"}
                    </td>
                    <td class='text-end'><a href="/staff/view/${usuarios.id}/" type="button" class="btn btn-dark btn-sm">View</a></td>
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

function delete_user(id) {
    $('#modal_user_delete').modal('show');
    $('#delete_id').val(id);
}
function modal_user_password_update(id) {
    $('#modal_user_password_update').modal('show');
    $('#update_id').val(id);
}
function confirm_delete_user() {
    var id = $('#delete_id').val();
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    fetch(`/configuracion/staff/delete/${id}/`, {
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