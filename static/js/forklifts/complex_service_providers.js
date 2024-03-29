let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [0, 2] },
        { searchable: false, targets: [0, 2] }
    ],
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listFrokslifts();

    dataTable = $("#datatable-contenido").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listFrokslifts = async () => {
    try {
        const response = await fetch("/forklifts/json/pull/serviceproviders/");
        const data = await response.json();

        let content = ``;
        data.providers_data.forEach((val, index) => {
            content += `
                <tr>
                    <td class="align-middle"><img height="50px" src="/media/${val.imagen}"</td>
                    <td class="align-middle">${val.name}</td>
                    <td class='text-end align-middle'>
                        <a href="view/${val.id}/" class="btn btn-dark btn-sm">View</a>
                    </td>
                </tr>`;
        });
        tableContenido_results.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});
