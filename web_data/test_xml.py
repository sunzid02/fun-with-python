import xml.etree.ElementTree as ET

data = '''<person>
            <name> Sunzid </name>
            <phone type="intl"> +1 734 303 4456 </phone>
            <email hide="yes"/>
        </person>'''

tree = ET.fromstring(data)

# print( 'Name: ', tree.find('name').text )
# print( 'Attr: ', tree.find('email').get('hide') )


input = '''<stuff>
        <users>
            <user x="7">
                <id>009</id>
                <name>xyz</name>
            </user>        
            <user x="9">
                <id>005</id>
                <name>she</name>
            </user>        
        </users>
    </stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #returns a list
print(lst)    

for item in lst:
    print('Name: ', item.find('name').text)
    print('id: ', item.find('id').text)
    print('Attribute: ', item.get('x'))
