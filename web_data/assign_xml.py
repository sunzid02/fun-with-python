import xml.etree.ElementTree as ET

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/comments_423417.xml'
xml = urlopen(url, context=ctx).read()
sum = 0


commentInfo = ET.fromstring(xml)
lst = commentInfo.findall('comments/comment')  # returns a list

for item in lst:
    sum = sum + int(item.find('count').text)


print(sum)


