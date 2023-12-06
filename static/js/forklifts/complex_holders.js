let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [0, 2, 3] },
        { searchable: false, targets: [0, 2, 3] }
    ],
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listForklifts();

    dataTable = $("#datatable-contenido").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listForklifts = async () => {
    try {
        const response = await fetch("/forklifts/json/pull/holders/");
        const data = await response.json();

        let content = ``;
        data.owners.forEach((owner) => {
            content += `
                <tr>
                    <td class="align-middle"><img height="50px" src="/media/${owner.imagen}"></td>
                    <td class="align-middle">${owner.name}</td>
                    <td class="align-middle"><button type="button" onclick="loadContentStatus(${owner.id})" class="btn btn-sm btn-primary">${owner.num_forklifts} Forklifts</button><br></button></td>
                    <td class='text-end align-middle'><a href="view/${owner.id}" class="btn btn-dark btn-sm">View</a></td>
                </tr>`;
        });
        $("#tableContenido_results").html(content);
    } catch (ex) {
        alert(ex);
    }
};

const renderStatuses = (statuses) => {
    let statusHtml = '';
    statuses.forEach((status) => {
        statusHtml += `<div>${status.name} - ${status.num_statuses}</div>`;
    });
    return statusHtml;
};

window.addEventListener("load", async () => {
    await initDataTable();
});

function loadContentStatus(id) {
    url = '/forklifts/json/pull/status/' + id;
    divId = '#frk_status_count'; 
    $(divId).load(url);
    $('#StatusModal').modal('show');
}