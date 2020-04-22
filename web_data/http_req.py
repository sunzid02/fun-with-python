import socket


# create the doorway from your pc
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create the connection
con = mysock.connect(('data.pr4e.org', 80))

#request for data, so send 
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(100)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

print("hello world")