import threading
import time
import random

"""
线程锁的本质：只有当加了锁的线程执行完之后，其他线程才会继续执行
"""

gmoney = 1000
# 创建一个锁
glock = threading.Lock()
gtotaltimes = 10
gtimes = 0


class ProducerThread(threading.Thread):
    def run(self):
        global gmoney
        global gtimes
        while True:
            money = random.randint(100, 1000)
            # 因为这是改变全局变量的操作，所以需要加上锁
            glock.acquire()
            if gtimes >= gtotaltimes:
                # 一定要先释放锁，然后退出
                glock.release()
                break
            gmoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gmoney))
            gtimes += 1
            glock.release()
            time.sleep(2)


class ConsumerThread(threading.Thread):
    def run(self):
        global gmoney
        while True:
            money = random.randint(100, 1000)
            # 因为这是改变全局变量的操作，所以需要加上锁
            glock.acquire()
            if gmoney >= money:
                gmoney -= money
                print('%s消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gmoney))
            else:
                # 当生产者不继续生产的时候，就让消费者停止消费
                if gtimes >= gtotaltimes:
                    glock.release()
                    break
                print('%s消费者准备消费%d元钱，剩余%d元钱，不够花！' % (threading.current_thread(), money, gmoney))
            glock.release()
            time.sleep(2)


def main():
    '''
    1.创建5个生产者
    2.创建3个消费者
    '''
    for i in range(5):
        p = ProducerThread(name='生产者%s' % i)
        p.start()

    for i in range(3):
        c = ConsumerThread(name='消费者%s' % i)
        c.start()


if __name__ == '__main__':
    main()
