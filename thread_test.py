import threading
import time
# from datetime import datetime


def thread_func(val):  # 线程函数
    return val+1


if __name__ == '__main__':
    # start = datetime.today().now()
    start = time.time()

    threads = []
    for i in range(10):  # 循环创建500个线程
        t = threading.Thread(target=thread_func, args=(i,))
        threads.append(t)

    for t in threads:  # 循环启动500个线程
        t.start()

    print(threads)
    duration = time.time() - start
    print(duration)
