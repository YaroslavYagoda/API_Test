import requests

url = 'https://api.chucknorris.io/jokes/random'
print(f'URL запроса:"{url}"')

result = requests.get(url)
assert 200 == result.status_code, f'Ошибка, получен код ответа: {result.status_code}'
print('Статус код: 200')

result.encoding = 'utf-8'
print(result.json())
