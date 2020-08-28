''' JavaScript Object Notation '''
import json
people_string = '''
{
    "people": [
        {
            "name": "Vasif Qarayev",
            "phone": "+994505555555",
            "emails": ["vasif@gmail.com", "vasif@mail.ru"],
            "work_experience": true
        },
        {
            "name": "Nail Cebiyev",
            "phone": "+994506666666",
            "emails": null,
            "work_experience": false
        }
    ]
}
'''
# convert json to dict
data = json.loads(people_string)

# we get names from our new dict
for person in data['people']:
    print(person['name'])

# we remove phone numbers and convert back to json
for person in data['people']:
    del person['phone']

''' intend for formatting, for readibility '''
new_string = json.dumps(data, indent = 2)
print(new_string)