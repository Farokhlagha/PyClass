import threading
import time

# class Farok:     
#     def anything():
#         ...


class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):          # run is neseccery
        for i in range(10):
            print(self.name)
            time.sleep(0.5)

t1 = MyThread('Ali')
t2 =MyThread('Farok')

t1.start()
t2.start()