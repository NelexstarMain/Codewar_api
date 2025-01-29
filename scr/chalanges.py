import requests

USER = "NelexstarMain"
PAGE = 1
URL = f"https://www.codewars.com/api/v1/users/{USER}/code-challenges/completed?page=0"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    completed = data.get('data')
    for chalanege in completed:
        print(chalanege.get('id'))
else:
    print(f"Nie udało się pobrać danych. Kod błędu: {response.status_code}")
