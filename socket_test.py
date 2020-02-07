# ok

import socket
# 获取本机的ip地址
def get_addr():
    # 获取本机计算机名称
    hostname = socket.gethostname()
    # 获取本机ip并返回
    return socket.gethostbyname(hostname)

# AF_INET表示ip地址的类型是ipv4，
# SOCK_DGRAM表示传输的协议类型是udp
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地信息，若不绑定，系统会自动分配
host = get_addr()
bind_addr = (host, 3100)
print('bind_addr = ', bind_addr)
udp_socket.bind(bind_addr)  # ip和port，ip一般不用写，表示本机的任何一个ip

while True:
    # 等待接收数据
    revc_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # 回传数据
    udp_socket.sendto(revc_data[0], revc_data[1])
    if revc_data[0] == b'quit':
        break
    # 打印接收到的数据
    # print('revc_data = ', revc_data)
    # print('data = ', revc_data[0])
    # print('ip_port = ', revc_data[1])

udp_socket.close()      # 关闭套接字
