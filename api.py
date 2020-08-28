import json
import requests
from urllib.request import urlopen

# ready api for curresies converting
with urlopen("https://swapi.dev/api/people") as response:
    source = response.read()



# response from api converted to dict
data = json.loads(source)

# get as json formatted
# print(json.dumps(data, indent=2))

# below I don't get same number
# print((data['count']))
# print(len(data['results']))

for people in data['results']:
    name = people['name']
    height = people['height']
    print(f"name: {name} / height: {height}")