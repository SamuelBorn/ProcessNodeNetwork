from enum import Enum

from ProcessNodeNetworkPlan.logic.Edge import Edge
from ProcessNodeNetworkPlan.logic.Process import Process


def build_graph_from_json(json):
    g = Graph()
    for row in json.get("rows"):
        g.add_process(row.get("#"), row.get("Dauer"))
    for row in json.get("rows"):
        for predecessor, min_constraint, max_constraint in zip(row.get("Vorgänger"), row.get("Mindestabstand"), row.get("Maximalabstand")):
            if min_constraint:
                g.add_min_edge(predecessor, row.get("#"), min_constraint)
            if max_constraint:
                g.add_max_edge(predecessor, row.get("#"), max_constraint)

    print(g)


class Graph:
    def __init__(self):
        self.processes = []
        self.edges = []

    def get_pids(self):
        return [process.pid for process in self.processes]

    def get_process(self, pid):
        for process in self.processes:
            if process.pid == pid:
                return process
        raise Exception("PID NOT IN GRAPH")

    def add_process(self, pid, duration):
        if pid in self.get_pids():
            raise Exception("PID ALREADY IN GRAPH")
        self.processes.append(Process(pid, duration))

    def add_min_edge(self, from_pid, to_pid, time_constraint):
        if from_pid not in self.get_pids() or to_pid not in self.get_pids():
            raise Exception(f"PID {from_pid} or {to_pid} NOT IN GRAPH")
        self.edges.append(Edge(self.get_process(from_pid), self.get_process(to_pid), time_constraint))

    def add_max_edge(self, from_pid, to_pid, time_constraint):
        if from_pid not in self.get_pids() or to_pid not in self.get_pids():
            raise Exception("PID NOT IN GRAPH")
        self.edges.append(
            Edge(self.get_process(to_pid), self.get_process(from_pid),
                 -time_constraint - self.get_process(to_pid).duration - self.get_process(from_pid).duration))

    def __str__(self):
        return f"Prozesse: {self.processes}\nKanten: {self.edges}"
