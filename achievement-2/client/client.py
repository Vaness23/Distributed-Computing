import requests

url = "http://localhost"
myjson = input()

req = requests.post(url, json=myjson)

print(req.status_code)
print(req.json())