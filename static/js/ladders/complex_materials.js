let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [0,1] },
        { searchable: false, targets: [0,1]}
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
        const response = await fetch("/ladders/json/pull/materials/");
        const data = await response.json();

        let content = ``;
        data.materiales.forEach((val, index) => {
            content += `
                <tr>
                    <td class="align-middle"><span style="height: 18px;width: 18px;background-color:${val.color};border-radius: 50%;vertical-align: sub;display: inline-block;" class="dot"></span> ${val.name}</td>
                    <td class='text-end align-middle'><a href="view/${val.id}/" class="btn btn-dark btn-sm">View</a></td>
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