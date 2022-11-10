import requests
import json

BASE = "http://localhost:5000/"

response = requests.put(BASE+"/video/1", {"name": "Hi", "likes": 20, "views": 1000})
print(response.json())

response = requests.get(BASE+"/video/1")
print(response.json())

response = requests.get(BASE+"/video/2")
print(response.json())

response = requests.delete(BASE+"/video/2")
print(response.json())

response = requests.delete(BASE+"/video/1")
print(response)

