class Song:
    def __init__(self, s_name: str, length: float, single: bool):
        self.single = single
        self.length = length
        self.s_name = s_name

    def get_info(self):
        return f"{self.s_name} - {self.length}"
