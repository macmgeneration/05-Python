import requests

url = 'http://localhost:8000'

while True:
    text = input('Ingrese un texto: ')
    if text == 'end':
        break
    response = requests.get(url, params={'text': text})

    print(response.text)