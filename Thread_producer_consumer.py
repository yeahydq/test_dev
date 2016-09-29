#!/usr/bin/env python
# -*- coding:utf-8 -*-

import thread, threading
import urllib2
import time, random
import Queue

share_queue = Queue.Queue()  #共享队列
my_lock = thread.allocate_lock()
class Producer(threading.Thread) :

    def run(self) :
        products = range(5)
        global share_queue
        while True :
            num = random.choice(products)
            my_lock.acquire()
            share_queue.put(num)
            print  "Produce : ", num
            my_lock.release()
            time.sleep(random.random())

class Consumer(threading.Thread) :

    def run(self) :
        global share_queue
        while True:
            my_lock.acquire()
            if share_queue.empty() : #这里没有使用信号量机制进行阻塞等待,
                print "Queue is Empty..."
                my_lock.release()
                time.sleep(random.random())
                continue
            num = share_queue.get()
            print "Consumer : ", num
            my_lock.release()
            time.sleep(random.random())

def main() :
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()

if __name__ == '__main__':
    main()
