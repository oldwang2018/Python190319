from socket import *
from time import ctime,sleep

host =''
port = 1200
buffsize = 2048
ADDR = (host,port)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer .bind(ADDR)
tcpServer .listen(3)

while True:
    print('Wait for connection ...')
    tctimeClient,addr = tcpServer .accept()
    print("Connection from :",addr)

    while True:
        data = tctimeClient.recv(buffsize).decode()
        print('recive....',data)
        if not data:
            break
        tctimeClient.send(data.encode())
    tctimeClient.close()
#tctimeClient.close()
#tcpServer.close()
