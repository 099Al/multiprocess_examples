# SuperFastPython.com
# example of sharing data with the callback function
from random import random
from time import sleep
from multiprocessing.pool import Pool


# result callback function
def result_callback(result):
    global data
    # report shared global data from main process
    print(f'Callback data: {data}', flush=True)
    # change it
    data = random()
    # report changed global data
    print(f'Callback data now: {data}', flush=True)


# task executed in a worker process
def task(identifier):
    sleep(1)


# protect the entry point
if __name__ == '__main__':
    # prepare shared global data
    data = random()
    print(f'Main data: {data}', flush=True)
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool
        result = pool.apply_async(task, args=(0,), callback=result_callback)
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()
    # report shared global data again
    print(f'Main data: {data}', flush=True)