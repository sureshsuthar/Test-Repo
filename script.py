import requests

r = requests.get('https://google.co.in')
print(r.status_code)
