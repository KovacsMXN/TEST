let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [3, 4, 5, 6, 7] },
        { searchable: false, targets: [3, 4, 5, 6, 7]}
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
        const response = await fetch("/configuracion/staff/ajax/request/");
        const data = await response.json();

        let content = ``;
        data.usuarios.forEach((usuarios, index) => {
            content += `
                <tr>
                    <td>${usuarios.first_name}</td>
                    <td>${usuarios.last_name}</td>
                    <td>${usuarios.username}</td>
                    <td>${usuarios.is_staff >= true 
                        ? "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-check-circle' viewBox='0 0 16 16'><path d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'/><path d='M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z'/></svg>" 
                        : "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-x-circle' viewBox='0 0 16 16'><path d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'/><path d='M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z'/></svg>"}
                    </td>
                    <td>${usuarios.is_active >= true 
                        ? "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-check-circle' viewBox='0 0 16 16'><path d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'/><path d='M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z'/></svg>" 
                        : "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-x-circle' viewBox='0 0 16 16'><path d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'/><path d='M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z'/></svg>"}
                    </td>
                    <td>${usuarios.is_superuser>= true 
                        ? "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-check-circle' viewBox='0 0 16 16'><path d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'/><path d='M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z'/></svg>" 
                        : "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-x-circle' viewBox='0 0 16 16'><path d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z'/><path d='M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z'/></svg>"}
                    </td>
                    <td>${usuarios.last_login}</td>
                    <td class='text-end'><a href="/configuracion/staff/edit/${usuarios.id}/" type="button" class="btn btn-dark">Edit</a> <a href="/configuracion/staff/edit/password/${usuarios.id}/" type="button" class="btn btn-dark">Update password</a> <button type="button" onClick="delete_user(${usuarios.id})" data-id="${usuarios.id}" href="/admin/auth/user/${usuarios.id}/delete/" type="button" class="btn btn-danger eliminar-registro">Delete</button></td>
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
                    //alert(data.mensaje);
                    // Puedes realizar alguna acción adicional después de la eliminación
                    // como recargar la página o actualizar la lista de registros
                })
                .catch(error => console.error('Error:', error));
    $('#modal_user_delete').modal('hide');
}