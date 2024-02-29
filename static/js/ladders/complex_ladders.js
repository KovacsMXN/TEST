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
        const response = await fetch("/ladders/json/pull/");
        const data = await response.json();

        let content = ``;
        data.ladders.forEach((ladder, index) => {
            content += `
                <tr>
                    <!-- CLAVE --><td>${ladder.clave}</td>
                    <!-- BRAND --><td><span style="height: 18px;width: 18px;background-color: ${ladder.brand__color};border-radius: 0%;vertical-align: sub;display: inline-block;" class="dot"></span> ${ladder.brand__name}</td>
                    <!-- MODELO --><td>${ladder.modelo}</td>
                    <!-- PASOS --><td>${ladder.pasos}</td>
                    <!-- STATUS --><td><span style="height: 18px;width: 18px;background-color: ${ladder.status__color};border-radius: 0%;vertical-align: sub;display: inline-block;" class="dot"></span> ${ladder.status__name}</td>
                    <!-- material --><td><span style="height: 18px;width: 18px;background-color: ${ladder.material__color};border-radius: 100%;vertical-align: sub;display: inline-block;" class="dot"></span> ${ladder.material__name}</td>
                    <!-- AGREGADO --><td>${ladder.agregado}</td>
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
