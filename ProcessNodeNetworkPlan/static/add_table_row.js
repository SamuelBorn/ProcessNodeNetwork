var counter = 1;

function add_table_row() {
    counter++;
    console.log(counter)
    $('#process_input_table').find('tbody').append("<tr>\n" +
        "                <th scope=\"row\">"+counter+"</th>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "                <td contenteditable=\"true\"></td>\n" +
        "            </tr>");
}