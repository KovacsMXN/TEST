let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { orderable: false, targets: [6] },
        { searchable: false, targets: [6]}
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
        const response = await fetch("/equipment/json/request/");
        const data = await response.json();

        let content = ``;
        data.equipment.forEach((equipment, index) => {
            content += `
<div class="accordion accordion-flush" id="accordionFlushExample">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
                <tr>
                    <td>${equipment.name}</td>
                    <td>${equipment.brand__name}</td>
                    <td>${equipment.model}</td>
                    <td>${equipment.serial}</td>
                    <td>${equipment.location__name}</td>
                    <td>${equipment.fa_number}</td>
                    <td class='text-end'><a href="view/${equipment.id}/" type="button" class="btn btn-dark">View</a></td>
                </tr>
      </button>
    </h2>
    <div id="flush-collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
      <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.</div>
    </div>
  </div>
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