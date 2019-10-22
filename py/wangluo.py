#写一个套接字服务端
from socket import *
#创建一个套接字对象
sockfd=socket(AF_INET,SOCK_STREAM)
#绑定服务端地址
sockfd.bind(('0.0.0.0',8989))
#设置监听套
sockfd.listen(5)
while True:
    #创建连接套接字
    print("waiting for connecting...")
    connect,addr=sockfd.accept()
    print("connecting from",addr)
    while True:
        #消息接收
        data=connect.recv(5)
        print(data)
        if not data:
            break
        #发送消息
        n=connect.send(b'Receive your message')
        print(n)
    #关闭连接
    connect.close()
sockfd.close()
