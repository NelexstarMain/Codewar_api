import json

class Save:
    def __init__(self, katas, filename="katas.json"):
        self.katas = katas
        self.filename = filename

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.katas, file, indent=4, ensure_ascii=False)
    @property
    def load(filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                katas = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            katas = []
        return katas