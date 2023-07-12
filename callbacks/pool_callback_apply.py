# SuperFastPython.com
# example of a callback function for apply_async()
from random import random,randint
from time import sleep
from multiprocessing.pool import Pool


# result callback function
def result_callback(result):
    print(f'Callback got: {result}', flush=True)



# task executed in a worker process
def task(identifier):
    # generate a value
    value = randint(5,9)
    # report a message
    print(f'Task {identifier} executing with {value}', flush=True)
    # block for a moment
    sleep(value)
    # return the generated value
    return value*100


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool
        result = pool.apply_async(task, args=(0,), callback=result_callback)
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()