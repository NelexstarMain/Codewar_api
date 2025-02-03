import os
from typing import List, Dict, Any
class MainFolder:

    def __init__(self, path, folder) -> None:
        self.MAIN_NAME = folder
        self.path = path
        self.main_path = os.path.join(self.path, self.MAIN_NAME)
        self.folders = []

    def create(self) -> None:
        if not os.path.exists(self.path):
            os.mkdir(self.main_path)
            for i in range(1, 8):
                os.mkdir(os.path.join(self.main_path, f"{i} kyu"))

    def add_katas(self, katas: List[Dict[str, Any]]) -> None:
        for kata in katas:
            name = kata['slug']
            rank = kata['rank']['name']
            doc = kata['description']
            url = kata['url']

            file_path = os.path.join(self.main_path, rank, f"{name}.py")
            
            if not os.path.exists(file_path):
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                content = f'''"""
    Kata: {name}
    Difficulty: {rank}
    URL: {url}

    {doc}
    """
    '''
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)



