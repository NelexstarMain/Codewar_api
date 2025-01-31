import os

class MainFolder:

    MAIN_NAME = "CODEWAR"

    def __init__(self, path) -> None:
        self.path = path
        self.main_path = ""
        self.folders = []

    def create(self) -> None:
        if os.path.exists(self.path):
            os.mkdir(os.path.join(self.path, self.MAIN_NAME))
            self.main_path = os.path.join(self.path, self.MAIN_NAME)

            for i in range(1, 8):
                os.mkdir(os.path.join(self.main_path, f"{i}kyu"))



