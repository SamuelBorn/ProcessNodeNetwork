function load_example() {
    counter=9
    $("#process_input_table tbody tr").remove()
     $('#process_input_table').find('tbody').append("<tr>\n" +
         "                <td>1</td>\n" +
         "                <td contenteditable=\"true\">Baustelle einrichten</td>\n" +
         "                <td contenteditable=\"true\">2</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>2</td>\n" +
         "                <td contenteditable=\"true\">Bodenplatte</td>\n" +
         "                <td contenteditable=\"true\">3</td>\n" +
         "                <td contenteditable=\"true\">1</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>3</td>\n" +
         "                <td contenteditable=\"true\">Wasseranschluss</td>\n" +
         "                <td contenteditable=\"true\">3</td>\n" +
         "                <td contenteditable=\"true\">2</td>\n" +
         "                <td contenteditable=\"true\">-2</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>4</td>\n" +
         "                <td contenteditable=\"true\">Mauerarbeiten</td>\n" +
         "                <td contenteditable=\"true\">5</td>\n" +
         "                <td contenteditable=\"true\">2</td>\n" +
         "                <td contenteditable=\"true\">1</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>5</td>\n" +
         "                <td contenteditable=\"true\">Dach</td>\n" +
         "                <td contenteditable=\"true\">3</td>\n" +
         "                <td contenteditable=\"true\">4</td>\n" +
         "                <td contenteditable=\"true\">-</td>\n" +
         "                <td contenteditable=\"true\">3</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>6</td>\n" +
         "                <td contenteditable=\"true\">Wasser + Elektrik</td>\n" +
         "                <td contenteditable=\"true\">2</td>\n" +
         "                <td contenteditable=\"true\">3,4</td>\n" +
         "                <td contenteditable=\"true\">2,1</td>\n" +
         "                <td contenteditable=\"true\">-,-</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>7</td>\n" +
         "                <td contenteditable=\"true\">Isolierung</td>\n" +
         "                <td contenteditable=\"true\">4</td>\n" +
         "                <td contenteditable=\"true\">5,6</td>\n" +
         "                <td contenteditable=\"true\">-,1</td>\n" +
         "                <td contenteditable=\"true\">-,-</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>8</td>\n" +
         "                <td contenteditable=\"true\">Innenausbau</td>\n" +
         "                <td contenteditable=\"true\">3</td>\n" +
         "                <td contenteditable=\"true\">3,6</td>\n" +
         "                <td contenteditable=\"true\">-,-</td>\n" +
         "                <td contenteditable=\"true\">7,-</td>\n" +
         "            </tr>\n" +
         "            <tr>\n" +
         "                <td>9</td>\n" +
         "                <td contenteditable=\"true\">Einrichtung</td>\n" +
         "                <td contenteditable=\"true\">2</td>\n" +
         "                <td contenteditable=\"true\">7,8</td>\n" +
         "                <td contenteditable=\"true\">1,-</td>\n" +
         "                <td contenteditable=\"true\">-,-</td>\n" +
         "            </tr>")
}