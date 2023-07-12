# SuperFastPython.com
# example of using a barrier in the process pool that use a manager
from random import random
from time import sleep
from multiprocessing import Manager
from multiprocessing.pool import Pool
from multiprocessing import Barrier

# error callback function
def custom_error_callback(error):
    print(error, flush=True)

# task executed in a worker process
def task(identifier, barrier):
    # report waiting message
    print(f'Task {identifier} waiting...', flush=True)
    # wait for all other tasks
    barrier.wait()
    # generate a value
    value = random()
    # block for a moment
    sleep(value)
    # report a message
    print(f'Task {identifier} completed with {value}', flush=True)


# protect the entry point
if __name__ == '__main__':
    # create the manager
    #Без менеджера будет ошибка. Condition objects should only be shared between processes through inheritance
    '''
    multiprocessing.Manager instance.

    This will create and host a barrier variable 
    in a new server process and returns a proxy object 
    that can be shared among child worker processes 
    and used to interface with the centralized barrier instance.
    '''
    with Manager() as manager:
        # create the shared barrier
        barrier = manager.Barrier(4)
        # create and configure the process pool
        with Pool(4) as pool:
            # prepare task arguments
            items = [(i, barrier) for i in range(4)]
            # issue tasks into the process pool
            result = pool.starmap_async(task, items)
            # wait for all tasks to finish
            result.wait()
            # report done message
            print(f'Tasks done.', flush=True)
