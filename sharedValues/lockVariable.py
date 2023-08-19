import time

import time
from multiprocessing import Process, Value, Lock

def func(val,lock):

    for i in range(50):

        time.sleep(0.01)
        with lock as l:
            val.value += 1

if __name__ == '__main__':
    v = Value('i', 0)
    l = Lock()
    procs = [Process(target=func, args=(v,l)) for i in range(100)]

    for p in procs: p.start()
    for p in procs: p.join()

    print(v.value)
