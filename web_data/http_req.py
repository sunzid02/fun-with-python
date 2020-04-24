import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# import socket

# using socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# data = mysock.recv(512)
# print(data)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(), end='')

# mysock.close()


# using other library
# fhand = urllib.request.urlopen(
#     'http://data.pr4e.org/romeo.txt'
#     )


# counts = dict()

# for line in fhand:
#     words = line.decode().split()

#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# print(counts) 


# using soup
url = 'https://en.wikipedia.org/wiki/Main_Page'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup)

#get all a tag data
tags = soup('a')
# print(tags)
# for tag in tags:
#     print(tag.get('href', None ))
