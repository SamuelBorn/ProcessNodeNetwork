class Edge:
    def __init__(self, from_vertex, to_vertex, time_constraint):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.time_constraint = time_constraint

    def __str__(self):
        return f"(f:{self.from_vertex.pid}, tv:{self.to_vertex.pid}, tc:{self.time_constraint})"

    def __repr__(self):
        return self.__str__()