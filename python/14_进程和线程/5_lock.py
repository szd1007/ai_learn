import time, threading

#假定这是你的银行存款
balance = 0
#并发锁
lock = threading.Lock()


def change_it(n):
    #先存后取， 结果应该为0：
    global balance
    balance  = balance + int(n)
    balance = balance - int(n)

def run_thread(n):
    for i in range(10000000):
        change_it(n)

def run_thread_with_lock(n):
    for i in range(10000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
t1 = threading.Thread(target=run_thread_with_lock, args=(5,))
t2 = threading.Thread(target=run_thread_with_lock, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)