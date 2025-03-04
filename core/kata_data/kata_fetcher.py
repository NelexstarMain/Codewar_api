import requests

class UserKataInfo:
    def __init__(self, user: str) -> None:
        self.USER = user
        self.URL: str = f"https://www.codewars.com/api/v1/users/{self.USER}/code-challenges/completed?page=0"
        self.id_list: list = []

    def get(self) -> None:   
        response = requests.get(self.URL)

        if response.status_code == 200:
            data = response.json()
            completed = data.get('data')
            for chalanege in completed:
                self.id_list.append(chalanege.get('id'))
        else:
            print(f"Error Key: {response.status_code}")

class KataInfo:
    def __init__(self, id: int) -> None:
        self.ID = id
        self.URL = f"https://www.codewars.com/api/v1/code-challenges/{self.ID}"
        self.data = {}

    def get(self) -> None:
        
        response = requests.get(self.URL)

        if response.status_code == 200:
            self.data = response.json()
            
        else:
            print(f"Error Key: {response.status_code}")


