var counter = 1;

function add_table_row() {
    counter++;
    $('#process_input_table').find('tbody').append("<tr>\n" +
        "                <td>"+counter+"</td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "            </tr>");
}