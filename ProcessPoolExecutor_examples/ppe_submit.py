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


    #Вывод результата по мере выполнения процессов
    with ProcessPoolExecutor(workers) as executor:
        futures = [executor.submit(f_task, n,x) for n,x in enumerate(data)]


        for f in as_completed(futures):
            print(f.result())


        """
        #Вывод не совсем корректный в этом случае
        for f in futures:
            print(f.result())
        """
    end = datetime.datetime.now()
    print('duratin:', end - start)

    print('---2 variant---------')

    start = datetime.datetime.now()

    l_proc =[]
    with ProcessPoolExecutor(workers) as executor:
        for n, x in enumerate(data):
            ex = executor.submit(f_task2, n, x)
            l_proc.append(ex)

        #Вывод по мере выполнения
        for f in as_completed(l_proc):
            print(f.result())

        print('-----')

        # Вывод в последовательности запуска
        for f in l_proc:
            print(f.result())

    end = datetime.datetime.now()



    print('duratin:',end-start)

