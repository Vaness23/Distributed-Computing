import requests

url = "http://localhost:5000/post"
myjson = input()

req = requests.post(url, json=myjson)

print(req.status_code)
print(req.json())