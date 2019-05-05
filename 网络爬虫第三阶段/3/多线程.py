
import threading
import time


#多线程执行的两种方式


'''

#第一种方式
def coding():
    for x in range(3):
        print('我是x-%s' %x)
        time.sleep(1)


def drawing():
    for y in range(3):
        print('我是y-%s' % y)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

'''

'''
#第二种方式
class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('我是x-%s' % x)
            time.sleep(1)


class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('我是y-%s' % x)
            time.sleep(1)

def main():
    t1 = CodingThread()
    t2 = DrawingThread()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

'''

'''
54953184801616
57221585758015
'''

x = 0

#创建一个锁
glock = threading.Lock()

def change_val():
    global x
    glock.acquire()
    for i in range(10000000):
        x+=i
    glock.release()
    print(x)


def main():
    for i in range(2):
        t = threading.Thread(target=change_val)
        t.start()

if __name__ == '__main__':
    main()