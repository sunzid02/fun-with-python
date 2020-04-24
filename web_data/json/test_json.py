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
print('Name:', info['name'])