import requests

url = "http://datamx.io/api/action/datastore_search?resource_id=9bf7b882-c533-43fa-9c85-33d411034d12&limit=5"
j = requests.get(url).json()
print(j)