import os
import datetime
from multiprocessing import Pool, Manager, cpu_count, current_process
import time
import random


def listener():

     proc = current_process()
     print('init',proc)



def copy_table(tbl,q,v):
    proc = current_process()
    print('task',proc)
    start = datetime.datetime.now().strftime('%H:%M:%S')
    w=random.randint(3,8)
    time.sleep(w)
    print(f'COPY E {tbl} start={start} wait={w},')
    #v.value += 1
    q.put(1)
    #print('.', v.value)

if __name__ == '__main__':
     tables_l = (x for x in ['1A', '2B', '3C', '4D', '5E', '6F', '7G', '8H'])
     #tables_l = ('T'+str(x) for x in range(0,100))     manager = Manager()
     manager = Manager()
     v = manager.Value('i',0)
     q = manager.Queue()
     q.put('start')
     with Pool(20,initializer=listener) as pool:
         _ = [pool.apply_async(copy_table,args=(tbl,q,v)) for tbl in tables_l]
         pool.close()
         pool.join()

     q.put('break')