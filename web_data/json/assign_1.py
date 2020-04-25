import json
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_423418.json'
urlData = urlopen(url, context=ctx).read().decode()
data = json.loads(urlData)
sum = 0

#json beautifier print
print( json.dumps(data['comments'], indent=4) )


for item in data['comments']:
    sum = sum + item['count']


print(sum)
