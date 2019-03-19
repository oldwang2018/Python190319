import time, threading

def loop(x):
    print(x)
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('%s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


t = threading.Thread(target=loop,args=('aaa',), name='LoopThread')
t.start()


t2 = threading.Thread(target=loop,args=('bbb',), name='LoopThread2222')
t2.start()


