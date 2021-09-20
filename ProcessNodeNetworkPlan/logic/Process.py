class Process:
    def __init__(self, pid, duration):
        self.pid = pid
        self.duration = duration

    def __str__(self):
        return f"({self.pid}, d:{self.duration})"

    def __repr__(self):
        return self.__str__()
