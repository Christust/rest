import requests

endpoint = "http://127.0.0.1:8000/api/"

r = requests.get(endpoint, params={"abc": 123}, json={"query":"Hola"})

print(r.json())