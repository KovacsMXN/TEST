let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [] },
        { searchable: false, targets: []}
    ],
    destroy: true
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }

    await listFrokslifts();

    dataTable = $("#datatable-forklifts").DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listFrokslifts = async () => {
    try {
        const response = await fetch("/forklifts/api/pull/forklifts/");
        const data = await response.json();

        let content = ``;
        data.forklifts.forEach((forkslifts, index) => {
            content += `
                <tr>
                    <td>${forkslifts.clave}</td>
                    <td><span style="height: 18px;width: 18px;background-color: ${forkslifts.brand__color};border-radius: 0%;vertical-align: sub;display: inline-block;" class="dot"></span> ${forkslifts.brand__name}</td>
                    <td>${forkslifts.modelo}</td>
                    <td>${forkslifts.serial}</td>
                    <td><span style="height: 18px;width: 18px;background-color: ${forkslifts.status__color};border-radius: 100%;vertical-align: sub;display: inline-block;" class="dot"></span> ${forkslifts.status__name}</td>
                    <td>${forkslifts.owner__name}</td>
                    <td class='text-end'><a href="view/${forkslifts.id}" class="btn btn-dark btn-sm">View</a> <button type="button" class="btn btn-danger btn-sm">Delete</button></td>
                </tr>`;
        });
        tableForklifts_results.innerHTML = content;
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});