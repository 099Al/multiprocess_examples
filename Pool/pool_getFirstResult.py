# SuperFastPython.com
# example of getting the first result from the process pool with a queue
from random import random
from time import sleep
from multiprocessing.pool import Pool
from multiprocessing import SimpleQueue


# worker process initialization
def init_worker(arg_queue):
    # define global variable for each worker
    global queue
    # store queue in global argument
    queue = arg_queue


# task executed in a worker process
def task(identifier):
    # generate a value
    value = 2 + random() * 10
    # report a message
    print(f'Task {identifier} started with parameter {value}', flush=True)
    # block for a moment
    sleep(value)
    # return the generated value
    queue.put((identifier, value))


# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = SimpleQueue()
    # create and configure the process pool
    with Pool(initializer=init_worker, initargs=(queue,)) as pool:
        # issue many tasks
        _ = pool.map_async(task, range(30))
        # get the first result, blocking
        identifier, value = queue.get()
        # report the first result
        print(f'First result: identifier={identifier}, value={value}')
        # terminate remaining tasks
        print('Terminating remaining tasks')