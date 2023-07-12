# SuperFastPython.com
# example of using a barrier in the process pool as a global variable
from random import random
from time import sleep
from multiprocessing import set_start_method
from multiprocessing import Barrier
from multiprocessing.pool import Pool


# task executed in a worker process
def task(identifier):
    # report waiting message
    print(f'Task {identifier} waiting...', flush=True)
    # wait for all other tasks via the inherited global variable
    barrier.wait()
    # generate a value
    value = random()
    # block for a moment
    sleep(value)
    # report a message
    print(f'Task {identifier} completed with {value}', flush=True)


# protect the entry point
if __name__ == '__main__':
    # set the fork start method
    set_start_method('fork')
    # create the shared barrier
    barrier = Barrier(4)
    # create and configure the process pool
    with Pool(4) as pool:
        # issue tasks into the process pool
        result = pool.map_async(task, range(4))
        # wait for all tasks to finish
        result.wait()
        # report done message
        print(f'Tasks done.', flush=True)