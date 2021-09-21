from ProcessNodeNetworkPlan.logic.Graph import Graph
from ProcessNodeNetworkPlan.logic.ResultContainer import ResultContainer
from ProcessNodeNetworkPlan.logic.ResultContainerList import ResultContainerList
from math import inf
import queue


class ComputeMinMaxTime:

    def __init__(self, graph: Graph):
        self.graph = graph
        self.results = ResultContainerList(graph.get_processes())

    def compute_sxz_and_fxz(self):
        self.compute_fxz()
        self.compute_sxz()
        return self.results

    # VORLESUNG SEITE 29
    # CAN ONLY BE CALLED WHEN COMPUTE FXZ WAS CALLED
    def compute_sxz(self):
        q = []
        for process in self.graph.get_processes():
            self.results.set_sez(process, inf)
        q.insert(0, self.graph.get_end_process())
        end_process = self.graph.get_end_process()
        self.results.set_sez(end_process, self.results.get_fez(end_process))
        self.results.set_saz(end_process, self.results.get_sez(end_process) - end_process.duration)
        finished = False

        while not finished:
            q_a = q[0]
            for j in self.graph.get_immediate_predecessors(q_a):
                if self.results.get_sez(j) > self.results.get_saz(q_a) - self.graph.get_edge(j, q_a).time_constraint:
                    self.results.set_sez(j, self.results.get_saz(q_a) - self.graph.get_edge(j, q_a).time_constraint)
                    self.results.set_saz(j, self.results.get_sez(j) - j.duration)
                    if j not in q:
                        q.insert(len(q), j)
            if q[0] != q[-1]:
                q.pop(0)
            else:
                finished = True

    # VORLESUNG SEITE 29
    def compute_fxz(self):
        q = []
        for process in self.graph.get_processes():
            self.results.set_faz(process, -inf)
        q.insert(0, self.graph.get_start_process())
        self.results.set_faz(self.graph.get_start_process(), 0)
        self.results.set_fez(self.graph.get_start_process(), self.graph.get_start_process().duration)
        finished = False

        while not finished:
            q_a = q[0]
            for j in self.graph.get_immediate_successors(q_a):
                if self.results.get_faz(j) < self.results.get_fez(q_a) + self.graph.get_edge(q_a, j).time_constraint:
                    self.results.set_faz(j, self.results.get_fez(q_a) + self.graph.get_edge(q_a, j).time_constraint)
                    self.results.set_fez(j, self.results.get_faz(j) + j.duration)
                    if j not in q:
                        q.insert(len(q), j)
            if q[0] != q[-1]:
                q.pop(0)
            else:
                finished = True
