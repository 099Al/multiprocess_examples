import os
import datetime
from multiprocessing import Pool, Manager, cpu_count
import time
import random





def res(x):
    v.value += 1
    print('.',v.value)


def copy_table(tbl):
    start = datetime.datetime.now().strftime('%H:%M:%S')
    w=random.randint(3,8)
    #print(f'COPY S {tbl} start={start}')
    time.sleep(w)
    print(f'COPY E {tbl} start={start} wait={w},')








if __name__ == '__main__':
    #tables_l = (x for x in ['1A', '2B', '3C', '4D', '5E', '6F', '7G', '8H'])
    tables_l = ('T'+str(x) for x in range(0,100))

    manager = Manager()
    v = manager.Value('i',0)

    with Pool(8) as pool:
        result = [pool.apply_async(copy_table, args=(x,) , callback=res) for x in tables_l]

        pool.close()
        pool.join()



