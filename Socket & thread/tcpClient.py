from socket  import *
from time import sleep
HOST ='127.0.0.1'
PORT = 1200
BUFFSIZE=2048
ADDR = (HOST,PORT)

tctimeClient = socket(AF_INET, SOCK_STREAM)
tctimeClient.connect(ADDR)

while True:
    while True:
        str = input(">")
        if not str:
            break
        tctimeClient.send(str.encode())
    
    data = tctimeClient.recv(BUFFSIZE).decode() #阻塞
    if not data:
        break
    print('receive',data)
    
tctimeClient.close()
