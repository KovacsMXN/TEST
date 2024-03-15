let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [6] },
        { searchable: false, targets: [] }
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
        const response = await fetch("/scales/json/pull/");
        const data = await response.json();

        let content = ``;
        data.ladders.forEach((ladder, index) => {
            content += `
                <tr>
                    <!-- CLAVE --><td>${ladder.clave}</td>
                    <!-- CAPACIDAD --><td>${ladder.pesomax}</td>
                    <!-- BRAND --><td><span style="height: 18px;width: 18px;background-color: ${ladder.brand__color};border-radius: 0%;vertical-align: sub;display: inline-block;" class="dot"></span> ${ladder.brand__name}</td>
                    <!-- MODELO --><td>${ladder.modelo}</td>
                    <!-- SERIAL --><td>${ladder.serial}</td>
                    <!-- nMAX --><td>${ladder.nmax}</td>
                    <!-- CLASE --><td>${ladder.clase}</td>
                    <!-- POWER SUPLY --><td>${ladder.powersupply}</td>
                    <!-- STATUS --><td><span style="height: 18px;width: 18px;background-color: ${ladder.status__color};border-radius: 50%;vertical-align: sub;display: inline-block;" class="dot"></span> ${ladder.status__name}</td>
                    <td class='text-end'>
                        <a href="view/${ladder.id}" class="btn btn-dark btn-sm">View</a>
                    </td>
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
