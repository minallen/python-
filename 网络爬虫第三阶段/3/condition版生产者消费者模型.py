import threading
import time
import random

"""
线程锁的本质：只有当加了锁的线程执行完之后，其他线程才会继续执行
"""
gmoney = 1000
# 创建一个condition锁
gcondition = threading.Condition()
gtotaltimes = 10
gtimes = 0


class ProducerThread(threading.Thread):
    def run(self):
        global gmoney
        global gtimes
        while True:
            # 100-1000之内产生随机整数
            money = random.randint(100, 1000)
            # 因为这是改变全局变量的操作，所以需要加上锁
            gcondition.acquire()
            if gtimes >= gtotaltimes:
                # 一定要先释放锁，然后退出
                gcondition.release()
                break
            gmoney += money
            print('%s生产了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gmoney))
            gtimes += 1
            # 生产者生产完之后，通知等待的消费者线程准备接收锁
            gcondition.notify_all()
            gcondition.release()
            time.sleep(2)


class ConsumerThread(threading.Thread):
    def run(self):
        global gmoney
        while True:
            money = random.randint(100, 1000)
            # 因为这是改变全局变量的操作，所以需要加上锁
            gcondition.acquire()
            # 当准备消费的钱数不够的时候
            while gmoney < money:
                # 判断生产者执行的次数，当生产者不继续生产的时候，就让消费者停止消费
                if gtimes >= gtotaltimes:
                    # 释放锁，让消费者停止消费
                    gcondition.release()
                    return
                print('%s准备消费%d元钱，剩余%d元钱，不够花！' % (threading.current_thread(), money, gmoney))
                # condition版的锁有等待通知的功能
                gcondition.wait()
            gmoney -= money
            print('%s消费者消费了%d元钱，剩余%d元钱' % (threading.current_thread(), money, gmoney))
            gcondition.release()
            time.sleep(2)


def main():
    '''
    1.创建5个生产者
    2.创建3个消费者
    '''
    for i in range(3):
        c = ConsumerThread(name='消费者%s' % i)
        c.start()

    for i in range(5):
        p = ProducerThread(name='生产者%s' % i)
        p.start()


if __name__ == '__main__':
    main()
