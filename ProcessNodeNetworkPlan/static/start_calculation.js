$("#start_calculation_button").click(function () {
    $.ajax({
        url: "/",
        type: 'get',
        data: {
            row_json: JSON.stringify(table_to_json())
        },
        success: function (response) {
            console.log("SUCCESS");
        },
        error: function (xhr) {
            alert(JSON.parse(xhr.responseText).err_mes)
        }
    })
})

function table_to_json() {
    var rows = [];
    var $headers = $("th");
    var $rows = $("tbody tr").each(function (index) {
        $cells = $(this).find("td");
        rows[index] = {};
        $cells.each(function (cellIndex) {
            rows[index][$($headers[cellIndex]).html()] = $(this).html();
        });
    });

    var json_obj = {};
    json_obj.rows = rows;
    return json_obj;
}