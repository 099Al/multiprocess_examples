# SuperFastPython.com
# example of a callback function for map_async()
from random import random
from time import sleep
from multiprocessing.pool import Pool


# result callback function
def result_callback(res):
    # iterate over all results
    for item in res:
        print(f'Callback got: {item}', flush=True)


# task executed in a worker process
def task(identifier):
    # generate a value
    value = random()
    # report a message
    print(f'Task {identifier} executing with {value}', flush=True)
    # block for a moment
    sleep(value)
    # return the generated value
    return value


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool
        result = pool.map_async(task, range(5), callback=result_callback)
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()