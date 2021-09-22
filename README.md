# ProcessNodeNetwork

This tool is an add-on for my stipendium from the Nassau Central Studies Fund. I developed it in the course of the Operations Research lecture. 
The tool uses the django framework. Most of the logic is implemented in python. Frontend calls are handled with JavaScript (Ajax).


## Installation (Linux)

1. git clone https://github.com/SamuelBorn/ProcessNodeNetwork.git
2. cd ProcessNodeNetwork
3. pip install -r ./requirements.txt
4. python3 manage.py runserver
5. open http://127.0.0.1:8000/ in your browser


## Usage

It is possible to add any number of additional processes using the "Weiteren Prozess hinzufügen" button.
A process can be given a name and a duration.
Both fields can also be left blank.

In addition, any number of predecessor processes can be added to each process. Each predecessor must be assigned a minimum and maximum distance. If you do not want to specify one, you can also use a "-" to leave it open. The input is done by separated commas.

Example:
Predecessor: 3,4,5
Minimum distance: -,2,1
Maximum distance: -,-,3

This process has three predecessors: 3,4,5.
Predecessor 3 is not limited in minimum or maximum distance. We assume here that the minimum distance is 0.
Predecessor 4 has a minimum distance of 2 but no maximum distance.
Predecessor 5 has both a minimum distance of 1 and a maximum distance of 3.

At the end you get the calculated results for FAZ, FEZ, SEZ, SAZ. (more detailed explanations in the tooltip of the results)

## Additional Information

The algorithms of chapter 4, slides 29 and 30 were implemented in the script which can be found in extracts (for easy reference) in this repo.
The implementation can be found under ./ProcessNetworkPlan/logic/ComputeMinMaxTime.py

Special cases such as multiple potential start and end nodes were also considered.
There is also an algorithm that intercepts positive circles of a graph.
Most of the input errors in the table have a very meaningful error message which is communicated to the user.
