# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = 'http://py4e-data.dr-chuck.net/known_by_Banan.html'
# url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0

# Retrieve all of the span tags
tags = soup('a')
# print(tags)

for tag in tags:
    position = position + 1

    if( position == 18):
        href = tag.get('href', None)
        print(href)
        break
    else:
        
        continue   




# repeat process 2
# url = input('Enter - ')
html = urlopen(href, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0

# Retrieve all of the span tags
tags = soup('a')
# print(tags)

for tag in tags:
    position = position + 1

    if(position == 18):
        href = tag.get('href', None)
        print(href)
        break
    else:
        
        continue

# repeat process 3
# url = input('Enter - ')
html = urlopen(href, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0

# Retrieve all of the span tags
tags = soup('a')
# print(tags)

for tag in tags:
    position = position + 1

    if(position == 18):
        href = tag.get('href', None)
        print(href)
        break
    else:        
        continue


# repeat process 4
# url = input('Enter - ')
html = urlopen(href, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0

# Retrieve all of the span tags
tags = soup('a')

# print(tags)

for tag in tags:
    position = position + 1

    if(position == 18):
        href = tag.get('href', None)
        desigredTag = tag
        print(href)
        break
    else:
        continue


# repeat process 5
# url = input('Enter - ')
html = urlopen(href, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0

# Retrieve all of the span tags
tags = soup('a')

# print(tags)

for tag in tags:
    position = position + 1

    if(position == 18):
        href = tag.get('href', None)
        desigredTag = tag
        print(href)
        break
    else:
        continue


# repeat process 6
# url = input('Enter - ')
html = urlopen(href, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0

# Retrieve all of the span tags
tags = soup('a')

# print(tags)

for tag in tags:
    position = position + 1

    if(position == 18):
        href = tag.get('href', None)
        desigredTag = tag
        print(href)
        break
    else:
        continue


# repeat process 7
# url = input('Enter - ')
html = urlopen(href, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 0

# Retrieve all of the span tags
tags = soup('a')

# print(tags)

for tag in tags:
    position = position + 1

    if(position == 18):
        href = tag.get('href', None)
        desigredTag = tag.text
        print(href)
        break
    else:
        continue

print(desigredTag)

