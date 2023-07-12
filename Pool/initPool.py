# SuperFastPython.com
# example of initializing workers in a process pool and reporting threads and processes
from time import sleep
from multiprocessing.pool import Pool
from multiprocessing import current_process
from threading import current_thread


# task executed in a worker process
def task():
    # get the current process
    process = current_process()
    # get the current thread
    thread = current_thread()
    # report a message
    print(f'Worker executing task, process={process.name}, thread={thread.name}', flush=True)
    # block for a moment
    sleep(1)


# initialize a worker in the process pool
def initialize_worker():
    # get the current process
    process = current_process()
    # get the current thread
    thread = current_thread()
    # report a message
    print(f'Initializing worker, process={process.name}, thread={thread.name}', flush=True)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool(2, initializer=initialize_worker) as pool:
        # issue tasks to the process pool
        for _ in range(4):
            pool.apply_async(task)
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()