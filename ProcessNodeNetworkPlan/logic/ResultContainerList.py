from ProcessNodeNetworkPlan.logic.ResultContainer import ResultContainer


class ResultContainerList:

    # 𝐹𝐴𝑍 𝑖 Frühestmöglicher Anfangszeitpunkt von Vorgang 𝑖
    # 𝐹𝐸𝑍 𝑖 Frühestmöglicher Endzeitpunkt von Vorgang 𝑖
    # 𝑆𝐴𝑍 𝑖 Spätestmöglicher Anfangszeitpunkt von Vorgang 𝑖
    # 𝑆𝐸𝑍 𝑖 Spätestmöglicher Endzeitpunkt von Vorgang 𝑖
    def __init__(self, processes):
        self.results = [ResultContainer(process) for process in processes]

    def __str__(self):
        ret = "\n"
        for result in self.results:
            ret += f"{result}\n"
        return ret + "\n"

    def set_faz(self, process, new_faz):
        for result_container in self.results:
            if result_container.process == process:
                result_container.FAZ = new_faz
                return

    def set_fez(self, process, new_fez):
        for result_container in self.results:
            if result_container.process == process:
                result_container.FEZ = new_fez
                return

    def set_sez(self, process, new_sez):
        for result_container in self.results:
            if result_container.process == process:
                result_container.SEZ = new_sez
                return

    def set_saz(self, process, new_saz):
        for result_container in self.results:
            if result_container.process == process:
                result_container.SAZ = new_saz
                return

    def get_faz(self, process):
        for result_container in self.results:
            if result_container.process == process:
                return result_container.FAZ

    def get_fez(self, process):
        for result_container in self.results:
            if result_container.process == process:
                return result_container.FEZ

    def get_sez(self, process):
        for result_container in self.results:
            if result_container.process == process:
                return result_container.SEZ

    def get_saz(self, process):
        for result_container in self.results:
            if result_container.process == process:
                return result_container.SAZ
