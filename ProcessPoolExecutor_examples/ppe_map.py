import time
import datetime
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from random import randint

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
    print('task_out:','id:',n,'v=',x, 'ex_time:',end-start)
    return(n,x)

def f_task_v(x):
    start = datetime.datetime.now()
    time.sleep(x)
    end = datetime.datetime.now()

    #вывод на экран будет помере того, как отработает функция
    print('task_out:','v=',x, 'ex_time:',end-start)
    return x

if __name__ == '__main__':
    workers = multiprocessing.cpu_count()
    data = rand_list(10, 12)

    start = datetime.datetime.now()

    """
    with ProcessPoolExecutor(workers) as executor:
        futures = executor.map(f_task, range(10),data)

    print('-----map result-----')
    #Результат будут в порядке следования
    for fut in futures:
        print(fut)
    """

    #Второй вариант вывода результата
    with ProcessPoolExecutor(workers) as executor:
        for x in executor.map(f_task, range(10),data):
            print(x)

    end = datetime.datetime.now()

    print('duratin:',end-start)

