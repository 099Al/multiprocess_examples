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
        v = randint(1,max_val)
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
    d = end-start
    return(n,x,d)

if __name__ == '__main__':
    workers = multiprocessing.cpu_count()
    data = rand_list(30, 6)

    print(data)

    start = datetime.datetime.now()


    l_proc =[]
    with ProcessPoolExecutor(workers) as executor:
        for n, x in enumerate(data):
            ex = executor.submit(f_task2, n, x)
            l_proc.append(ex)

        #Вывод по мере выполнения
        #for f in as_completed(l_proc):
        #    print(f.result())

        print('-----')

        step = 3
        s = 0
        for x in as_completed(l_proc):
            s=s+1
            # report the number of remaining tasks
            if s >= step:
                print(f'res={x.result()} About {len(executor._pending_work_items)} tasks remain') #,end="\r"
                s = 0

    end = datetime.datetime.now()



    print('duratin:',end-start)

