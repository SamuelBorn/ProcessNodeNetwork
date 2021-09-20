from enum import Enum


class Graph:
    GraphJsonEnum = Enum("GraphJsonEnum", "not_used")

    def __init__(self):
        self.processes = []
        self.edges = []

    @staticmethod
    def build_graph_from_json(self, json):
        for row in json.get("rows"):
            pass  # TODO
