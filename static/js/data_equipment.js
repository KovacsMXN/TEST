let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
    ],
    pageLength: 4,
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
        const response = await fetch("/equipment/json/request/");
        const data = await response.json();

        let content = ``;
        data.equipment.forEach((equipment, index) => {
            content += `
                <tr>
                    <td>${equipment.id}</td>
                    <td>${equipment.fa_number}</td>
                    <td>${equipment.name}</td>
                    <td>${equipment.model}</td>
                    <td>${equipment.serial}</td>
                    <td>${equipment.description}</td>
                    <td>${equipment.brand_id}</td>
                    <td>${equipment.location_id}</td>
                </tr>`;
        });
        tableBody_programmers.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});