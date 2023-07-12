import os
import datetime
from multiprocessing import Pool, Manager, cpu_count
import time
import random

"""
Данныу пример не рабочий
т.к. инициализирующая функция не завершается
и код не может перейти к след шагу.
В init надо передавать только переменные или функцию, которая не должна повторяться.

Переменный передаются для каждого элеммента из pool ???
"""

def listener(q,v):
     while True:
         time.sleep(0.1)
         print('x')
         try:
             print('-1')
             el = q.get()
             print('-2')
             if el == 'break':
                 print('finished')
                 break
             v.value += 1
             print('v',v.value)
         except:
             print('--')



def copy_table(tbl,q,v):
     print('task')
     start = datetime.datetime.now().strftime('%H:%M:%S')
     w=random.randint(3,8)
     #print(f'COPY S {tbl} start={start}')
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
     with Pool(3,initializer=listener,initargs=(q,v)) as pool:
         _ = [pool.apply_async(copy_table,args=(tbl,q,v)) for tbl in tables_l]
         pool.close()
         pool.join()

     q.put('break')