import time
import datetime
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from random import randint
from concurrent.futures import as_completed

def rand_list(size,max_val=None):
    if max_val == None:
        max_val=size
    l = []
    for x in range(size):
        v = randint(5,max_val)
        l.append(v)
    return l

def f_task(n,x):
    start = datetime.datetime.now()
    time.sleep(x)
    end = datetime.datetime.now()
    #print('task_out:','id:',n,'v=',x, 'ex_time:',end-start)
    return(n,x)

def f_task2(n,x):
    start = datetime.datetime.now()
    time.sleep(x)
    end = datetime.datetime.now()
    #print('task_out:','id:',n,'v=',x, 'ex_time:',end-start)
    return(n,x)

if __name__ == '__main__':
    workers = multiprocessing.cpu_count()
    data = rand_list(10, 12)

    start = datetime.datetime.now()



    with ProcessPoolExecutor(workers) as executor:
        futures = [executor.submit(f_task, n,x) for n,x in enumerate(data)]


        print('-----')

        for x in as_completed(futures):
            # report the number of remaining tasks
            print(f'res={x.result()}About {len(executor._pending_work_items)} tasks remain')

        l_proc = []

        print()
        for x in futures:
            l_proc.append(x.result())

        print(sorted(l_proc,key=lambda x: x[0]))

    end = datetime.datetime.now()



    print('duratin:',end-start)

