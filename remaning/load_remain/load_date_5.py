import os
import datetime
from multiprocessing import Pool, Manager, cpu_count, Process
import time
import random


def init(q,v):
    global qG, vG
    qG = q
    vG = v

def listener(q,v):
    while True:
        #print(q.qsize())
        el = q.get()
        if el == None:
            print('finished')
            break
        v.value += 1
        print('.',v.value)

def copy_table(tbl):
    start = datetime.datetime.now().strftime('%H:%M:%S')
    w=random.randint(3,8)
    #print(f'COPY S {tbl} start={start}')
    time.sleep(w)
    print(f'COPY E {tbl} start={start} wait={w},')
    #v.value += 1
    qG.put(1)
    #print('.', v.value)

if __name__ == '__main__':
    tables_l = (x for x in ['1A', '2B', '3C', '4D', '5E', '6F', '7G', '8H'])
    #tables_l = ('T'+str(x) for x in range(0,100))
    manager = Manager()
    v = manager.Value('i',0)
    q = manager.Queue()
    process = Process(target=listener,args=(q,v))
    process.start()
    with Pool(3, initializer=init, initargs=(q,v)) as pool:
        result = [pool.apply_async(copy_table, args=(x,) ) for x in tables_l]
        pool.close()
        pool.join()
        q.put(None)