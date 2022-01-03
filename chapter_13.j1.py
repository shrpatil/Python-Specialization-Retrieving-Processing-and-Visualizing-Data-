import json

data = '''
{
    "name" : "Shreya",
    "phone": {
        "type":"intl",
        "num": "1234567890"
    },
    "email":{
        "hide":"yes"
    }
}'''

info = json.loads(data)
print("name: ", info["name"])
