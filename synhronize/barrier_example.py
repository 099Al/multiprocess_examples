from datetime import datetime
import time
import random

from threading import Thread
from threading import Barrier

def f(i,barrier):

    n = random.randint(0,6)
    print(f'f{i}',n)
    for x in range(0,n):
        time.sleep(x)
        print(f'func{i} all:{n} step{x}')
    print(f'func{i} DONE LOOP')


    barrier.wait()

    for x in range(0,3):
        print(f'func{i} step---------{x}')
    print(f'func{i} DONE')

if __name__ == '__main__':

    barrier = Barrier(3)

    for i in range(0,3):
        worker = Thread(target=f, args=(i,barrier))
        worker.start()
