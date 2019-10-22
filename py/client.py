from socket import *
#创建客户端套接字
socketcl=socket(AF_INET,SOCK_STREAM)
#建立连接
socketcl.connect(('192.168.1.104',8989))
while True:
    #发送消息
    n1=input("发送")
    if not n1:
        break
    n = socketcl.send(n1.encode('utf-8'))
    print(n)
    #接受消息
    data=socketcl.recv(1024)
    print("接收到",data.decode())
socketcl.close()