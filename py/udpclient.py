from socket import *
import sys
#创建数据报套接字
socketcl=socket(AF_INET,SOCK_DGRAM)
host=sys.argv[1]
port=int(sys.argv[2])
addr=(host,port)
while True:
    #发送消息
    data=input("发送")
    if not data:
        break
    socketcl.sendto(data.encode(),addr)
    #接收消息
    d1,addr1=socketcl.recvfrom(1024)
    print("从",addr1,"接收到：",d1.decode())
#关闭套接字
socketcl.close()