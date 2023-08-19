import os
import datetime
from multiprocessing import Pool, Manager
import time
import random





def copy_table(tbl):
    start = datetime.datetime.now().strftime('%H:%M:%S')
    w=random.randint(3,8)
    print(f'COPY S {tbl} start={start}')
    time.sleep(w)
    print(f'COPY E {tbl} start={start} wait={w},')








if __name__ == '__main__':
    tables_l = (x for x in ['1A', '2B', '3C', '4D', '5E', '6F', '7G', '8H'])

    with Pool(5) as pool:
        pool.map(copy_table, tables_l)



