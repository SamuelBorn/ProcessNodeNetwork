from enum import Enum

from ProcessNodeNetworkPlan.logic.Edge import Edge
from ProcessNodeNetworkPlan.logic.Process import Process


def build_graph_from_json(json):
    g = Graph()

    # add all processes
    for row in json.get("rows"):
        g.add_process(row.get("#"), row.get("Dauer"))

    # add all edges
    for row in json.get("rows"):
        for predecessor, min_constraint, max_constraint in zip(row.get("Vorgänger"), row.get("Mindestabstand"),
                                                               row.get("Maximalabstand")):
            if predecessor is not None:
                if min_constraint is not None:
                    g.add_min_edge(predecessor, row.get("#"), min_constraint)
                else:
                    g.add_min_edge(predecessor, row.get("#"), 0)
                if max_constraint is not None:
                    g.add_max_edge(predecessor, row.get("#"), max_constraint)

    # add pseudo end if multiple processes could be the last one
    if len(g.get_end_processes()) > 1:
        g.add_process(g.get_processes_count() + 1, 0)
        for end_process in g.get_end_processes():
            g.add_min_edge(g.get_processes_count(), end_process, 0)

    # add pseudo start if multiple processes could be the first one
    if len(g.get_start_processes()) > 1:
        # is lowest id
        g.add_process(0, 0)
        for start_process in g.get_start_processes():
            g.add_min_edge(start_process, g.get_processes_count(), 0)

    return g


class Graph:
    def __init__(self):
        self.processes = []
        self.edges = []

    def get_processes_count(self):
        return len(self.processes)

    def get_pids(self):
        return [process.pid for process in self.processes]

    def get_processes(self):
        return self.processes

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

    def get_edge(self, from_process, to_process):
        for edge in self.edges:
            if edge.from_vertex == from_process and edge.to_vertex == to_process:
                return edge
        raise Exception(f"EDGE FROM {from_process} to {to_process} NOT IN GRAPH")

    def get_start_process(self):
        if len(self.get_start_processes()) > 1:
            raise Exception(f"THERE ARE {self.get_start_processes()} STARTS")
        else:
            return self.get_start_processes()[0]

    def get_start_processes(self):
        start_processes = []
        for process in self.processes:
            if len(self.get_immediate_predecessors(process)) == 0:
                start_processes.append(process)
        return start_processes

    def get_end_processes(self):
        # Gets all processes that dont have a predecessor
        start_processes = []
        for process in self.processes:
            if len(self.get_immediate_successors(process)) == 0:
                start_processes.append(process)
        return start_processes

    def get_immediate_predecessors(self, process):
        # VORGÄNGER
        # gets all immediate predecessors, doesnt check if those predecessors has predecessors themself
        predecessors = []
        for edge in self.edges:
            if process == edge.to_vertex:
                predecessors.append(edge.from_vertex)
        return set(predecessors)

    def get_immediate_successors(self, process):
        # NACHFOLGER
        # gets all immediate predecessors, doesnt check if those predecessors has predecessors themself
        successors = []
        for edge in self.edges:
            if process == edge.from_vertex:
                successors.append(edge.to_vertex)
        return set(successors)

    def __str__(self):
        return f"Prozesse: {self.processes}\nKanten: {self.edges}"
