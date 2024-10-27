import requests

requests_headers = {
    'Accept_language' : 'ru'
}

response = requests.get('https://habr.com', headers=requests_headers)

print(response.text)