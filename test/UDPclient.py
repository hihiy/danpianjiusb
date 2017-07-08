from socket import *

HOST = '192.168.1.115'  # 主机名
PORT = 3000  # 端口号 与服务器一致
BUFSIZE = 1024  # 缓冲区大小1K
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:  # 无限循环等待连接到来
    try:
        # data = input('>')
        # if not data:
        #     break
        data = 'fffe123456789abcdef123456789abcdef12ffff'.encode('utf-8')
        # print(data)
        udpCliSock.sendto(data, ADDR)  # 发送数据
        # data, ADDR = udpCliSock.recvfrom(BUFSIZE)  # 接受数据
        # if not data:
        #     break
        # print('Server : ', data.decode('utf-8'))


    except Exception as e:
        print('Error: ', e)


udpCliSock.close()  # 关闭客户端