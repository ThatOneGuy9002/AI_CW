import json

with open("stations.json", "r") as file:
    data = json.load(file)

for item in data:
    print(item["stationName"])