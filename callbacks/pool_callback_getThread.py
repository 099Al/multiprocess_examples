# SuperFastPython.com
# example of reporting the process and thread that executes the callback function
from random import random
from time import sleep
from threading import current_thread
from multiprocessing import current_process
from multiprocessing.pool import Pool


# result callback function
def result_callback(result):
    # get the current process
    process = current_process()
    # report the details of the current process
    print(f'Callback Process: {process}', flush=True)
    # get the current thread
    thread = current_thread()
    # report the details of the current thread
    print(f'Callback Thread: {thread}', flush=True)


# task executed in a worker process
def task(identifier):
    # get the current process
    process = current_process()
    # report the details of the current process
    print(f'Task Process: {process}', flush=True)
    # get the current thread
    thread = current_thread()
    # report the details of the current thread
    print(f'Task Thread: {thread}', flush=True)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool
        result = pool.apply_async(task, args=(0,), callback=result_callback)
        # get the current process
        process = current_process()
        # report the details of the current process
        print(f'Main Process: {process}', flush=True)
        # get the current thread
        thread = current_thread()
        # report the details of the current thread
        print(f'Main Thread: {thread}', flush=True)
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()