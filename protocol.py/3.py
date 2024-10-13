import requests

search_parametrs = {
    'u': '',
    'T': ''
}
url = 'https://wttr.in'

response = requests.get(url, params=search_parametrs)

print(response.text)
