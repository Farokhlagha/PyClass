import threading
import time

def A(name, family):
    for i in range(10):
        print('Hello', name, family)
        time.sleep(1)


def B(name):
    for i in range(10):
        print('Bye Bye', name)
        time.sleep(1.5)


t1 = threading.Thread(target=A, args=['ali', 'zadeh'])
t2 = threading.Thread(target=B, args=['mamad'])

t1.start()
t2.start()