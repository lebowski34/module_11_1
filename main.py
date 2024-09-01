import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    print("Данные успешно получены!")

data = response.json()
print("Первый пост:")
print(data[0])

print("Заголовки ответа:")
print(response.headers)
