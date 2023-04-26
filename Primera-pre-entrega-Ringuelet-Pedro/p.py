import json
registro = {}

with open("db.json", "r") as file:
    registro = json.load(file)
print (registro)
