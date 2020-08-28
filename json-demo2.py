import json

# json.load() is used to read json from a file and json.loads() to read json from a string.

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(f"{state['name']} / {state['abbreviation']}")

# delete area_codes from our dict, and pass this to new created json file

for state in data['states']:
    del state['area_codes']

with open('newStates.json', 'w') as f:
    json.dump(data, f, indent=2)