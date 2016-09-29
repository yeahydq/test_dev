#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
类方法:
acquire()  #获得锁
release()  #释放锁
wait([timeout])  #持续等待直到被notify()或者notifyAll()通知或者超时(必须先获得锁),
wait()所做操作, 先释放获得的锁, 然后阻塞, 知道被notify或者notifyAll唤醒或者超时, 一旦被唤醒或者超时, 会重新获取锁(应该说抢锁), 然后返回
notify()  #唤醒一个wait()阻塞的线程.
notify_all()或者notifyAll()  #唤醒所有阻塞的线程
'''


import threading
import random, time, Queue

MAX_SIZE = 5
SHARE_Q = []  #模拟共享队列
CONDITION = threading.Condition()

class Producer(threading.Thread) :

    def run(self) :
        products = range(5)
        global SHARE_Q
        while True :
            CONDITION.acquire()
            if len(SHARE_Q) == 5 :
                print "Queue is full.."
                CONDITION.wait()
                print "Consumer have consumed something"
            product = random.choice(products)
            SHARE_Q.append(product)
            print "Producer : ", product
            CONDITION.notify()
            CONDITION.release()
            time.sleep(random.random())

class Consumer(threading.Thread) :

    def run(self) :
        global SHARE_Q
        while True:
            CONDITION.acquire()
            if not SHARE_Q :
                print "Queue is Empty..."
                CONDITION.wait()
                print "Producer have producted something"
            product = SHARE_Q.pop(0)
            print "Consumer :", product
            CONDITION.notify()
            CONDITION.release()
            time.sleep(random.random())

def main() :
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()

if __name__ == '__main__':
    main()
