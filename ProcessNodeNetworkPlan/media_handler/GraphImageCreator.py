import base64

import networkx as nx
import pylab
import os

from ProcessNodeNetworkPlan.logic.Graph import Graph


def get_image_base64(my_graph):
    create_image(my_graph)
    image_data = None
    with open("ProcessNodeNetworkPlan/media_handler/Graph.png", "rb") as image:
        image_data = base64.b64encode(image.read()).decode('utf-8')

    os.remove("ProcessNodeNetworkPlan/media_handler/Graph.png")
    return image_data


def create_image(my_graph: Graph):
    nx_graph = nx.DiGraph()

    print(my_graph.get_processes())

    for edge in my_graph.get_edges():
        from_name = f"{edge.from_vertex.pid} ({edge.from_vertex.duration})"
        to_name = f"{edge.to_vertex.pid} ({edge.to_vertex.duration})"
        weight = edge.time_constraint
        nx_graph.add_edge(from_name, to_name, weight=weight)

    edge_labels = dict([((u, v,), d['weight']) for u, v, d in nx_graph.edges(data=True)])

    pos = nx.circular_layout(nx_graph)
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, label_pos=0.6)
    nx.draw(nx_graph, pos, node_size=2000, node_color='#D8DEE9', with_labels=True, connectionstyle='arc3, rad = 0.0')

    pylab.savefig("ProcessNodeNetworkPlan/media_handler/Graph.png", format="PNG")
