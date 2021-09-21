class ResultContainer:
    def __init__(self, process):
        # 𝐹𝐴𝑍 𝑖 Frühestmöglicher Anfangszeitpunkt von Vorgang 𝑖
        # 𝐹𝐸𝑍 𝑖 Frühestmöglicher Endzeitpunkt von Vorgang 𝑖
        # 𝑆𝐴𝑍 𝑖 Spätestmöglicher Anfangszeitpunkt von Vorgang 𝑖
        # 𝑆𝐸𝑍 𝑖 Spätestmöglicher Endzeitpunkt von Vorgang 𝑖
        self.process = process
        self.FAZ = None
        self.FEZ = None
        self.SEZ = None
        self.SAZ = None

    def __str__(self):
        return f"P{self.process.pid}: {self.FAZ=}, {self.FEZ=}, {self.SEZ=}, {self.SAZ=}"
