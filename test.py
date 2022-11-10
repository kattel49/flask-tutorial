import requests

BASE = "http://localhost:5000/"

response = requests.get(BASE+"/helloworld/shubhushan/8049")
print(response.json())