from socket import *
from time import ctime

HOST = ''  # 主机名
PORT = 21567  # 端口号
BUFSIZE = 1024  # 缓冲区大小1K
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)  # 绑定地址到套接字

while True:  # 无限循环等待连接到来
    try:
        print('Waiting for message ....')
        data, addr = udpSerSock.recvfrom(BUFSIZE)  # 接受UDP
        print('Get client msg is: ', data.decode('utf-8'))

        # udpSerSock.sendto(('[%s] %s' % (ctime(), data.decode('utf-8'))).encode('utf-8'), addr)  # 发送UDP
        # print('Received from and returned to: ', addr)
    except Exception as e:
        print('Error: ', e)

udpSerSock.close()  # 关闭服务器