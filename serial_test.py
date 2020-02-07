# 利用虚拟串口根据vspd绑定COM5/COM6,虚拟成两台机通信。
# 在实际开发中需要用一个线程来处理接收数据
import threading
import serial           # pip install pyserial
import time
import sys
import queue            #队列一般用在线程数据交互


q = queue.Queue()


def read_data():
    try:
        # winsows系统使用com5口连接串行口
        ser = serial.Serial("COM5", 115200, timeout=0.02)
    except Exception as e:
        print("port select error=", e)
        sys.exit(1)                         # 异常终止,sys.exit() 正常终止
    else:
        print(ser.name)                     # check which port was really used
        while True:
            get_data = ser.read(1000)       # 阻塞在这里,这个函数比ser.read_all()好
            # ser.write(get_data)           #
            q.put(get_data)                 # 测试队列的用法
            if q.empty():
                pass    #占位作用，否则编译器报错
            else:
                ser.write(q.get())
        ser.close()


if __name__ == '__main__':
    t = threading.Thread(target=read_data)
    t.start()
    t.join()
    print("end")
