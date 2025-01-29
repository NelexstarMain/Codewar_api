import requests

class GetInformations:
    def __init__(self, user) -> None:
        self.USER: str = user
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

if __name__=="__main__":
    p = GetInformations("Elon_Musk")
    p.get()
    print(p.id_list)