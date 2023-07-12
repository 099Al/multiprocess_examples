# SuperFastPython.com
# example with the even chunksize
from math import ceil
from time import sleep
from random import random
from multiprocessing import Pool


# task to execute in a separate process
def task(arg):
    # generate a value
    value = random()
    # block for a fraction of a second
    sleep(1 + value)
    # return generated value combined with argument
    #print(arg,value)
    return arg + value


# protect the entry point
if __name__ == '__main__':
    # create the multiprocessing pool
    with Pool() as pool:
        # number of tasks to execute
        n_tasks = 30
        # chunksize to use
        n_tasks_per_chunk = ceil(n_tasks / len(pool._pool))
        # report details for reference
        print(f'chunksize={n_tasks_per_chunk}, n_workers={len(pool._pool)}')
        # issue tasks and process results

        #x = pool.map_async(task, range(100),chunksize=n_tasks_per_chunk)
        #x.wait()

        for result in pool.map(task, range(100), chunksize=n_tasks_per_chunk):
            # report the result
            print(result)