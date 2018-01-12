import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code
with open('abc.text', 'wb') as file:
    file.write(res.content)

