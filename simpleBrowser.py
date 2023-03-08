import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #create socket (phone)
mysock.connect(('data.pr4e.org',80)) #dial phone connect
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() #encode request to utf8 because python uses unicode
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()