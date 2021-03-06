$("#start_calculation_button").click(function () {
    $.ajax({
        url: "/",
        type: 'get',
        data: {
            row_json: JSON.stringify(table_to_json())
        },
        success: function (content) {
            $("#ajax_alerts").hide()
            $("#results_div").html(content)
        },
        error: function (xhr) {
            let content_div = $("#ajax_alerts")
            content_div.html("<div class=\"alert alert-danger mt-4\" role=\"alert\">Fehler: "+JSON.parse(xhr.responseText).err_mes+"</div>")
            content_div.show()
        }
    })
})

function table_to_json() {
    var rows = [];
    var $headers = $("#process_input_table th");
    var $rows = $("#process_input_table tbody tr").each(function (index) {
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