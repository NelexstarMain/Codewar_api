import json

class Save:
    def __init__(self, katas: str = None, path="katas.json"):
        self.katas = katas
        self.path = path

    def save(self):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.katas, file, indent=4, ensure_ascii=False)

    def load(self) -> list:
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                self.katas = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
        return self.katas
