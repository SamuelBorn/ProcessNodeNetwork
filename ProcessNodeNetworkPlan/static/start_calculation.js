$("#start_calculation_button").click(function () {
    $.ajax({
        url: "http://127.0.0.1:8000/",
        type: 'get',
        data: {
            action: "set_weight"
        }
    })
})