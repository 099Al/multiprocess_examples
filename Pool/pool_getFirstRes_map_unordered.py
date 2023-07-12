# SuperFastPython.com
# example of getting the first result from the process pool with imap_unordered
from random import random
from time import sleep
from multiprocessing.pool import Pool


# task executed in a worker process
def task(identifier):
    # generate a value
    value = 2 + random() * 10
    # report a message
    print(f'Task {identifier} executing with {value}', flush=True)
    # block for a moment
    sleep(value)
    # return the generated value
    return (identifier, value)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue many tasks
        it = pool.imap_unordered(task, range(30))
        # get the first result, blocking
        identifier, value = next(it)
        # report the first result
        print(f'First result: identifier={identifier}, value={value}')
        # terminate remaining tasks
        print('Terminating remaining tasks')