from socket import *
#创建数据报套接字
sockfd=socket(AF_INET,SOCK_DGRAM)
#绑定服务器地址
sockfd.bind(('0.0.0.0',9889))
while True:
    #接受消息
    data,addr=sockfd.recvfrom(1024)
    print("来自：",addr,"\t内容是：",data.decode())
    #发送消息
    d1='receive message!!!'
    sockfd.sendto(d1.encode(),addr)
#关闭套接字
sockfd.close()