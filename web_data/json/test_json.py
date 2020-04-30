import json 

data = '''
{
    "name": "chuck",
    "phone":{
        "type": "intl",
        "number": "01674569636"
    },
    "email":{
        "hide": "yes"
    }
}'''

info = json.loads(data)

list = info.items()

print(list)
print(json.dumps(info, indent=4))











