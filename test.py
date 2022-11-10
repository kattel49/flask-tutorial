import requests
import json

BASE = "http://localhost:5000/"

data = [
    {"likes": 100, "views": 1000, "name": "valla"},
    {"likes": 10, "views": 10000, "name": "villa"},
    {"likes": 1, "views": 10000, "name": "hunter x hunter"},
    {"likes": 102, "views": 10001, "name": "kill la kill"}
]

for i in range(len(data)):
    res = requests.put(BASE+f"/video/{i}", data[i])
    print(res.json())

res = requests.get(BASE+"/video/2")
print(res.json())

res = requests.get(BASE+"/video/100")
print(res.json())