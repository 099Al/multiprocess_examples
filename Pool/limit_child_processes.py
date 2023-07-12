"""
It is possible for child processes to become unstable
or accumulate resources without releasing them,
such as if there are subtle bugs in the tasks that are being executed.

As such, it is a good practice to limit the number
of tasks executed by each worker process
and create a new replacement worker process once the limit on the number of tasks has been reached.
"""

from time import sleep
from multiprocessing.pool import Pool
from multiprocessing import current_process


# task executed in a worker process
def task(value):
    # get the current process
    process = current_process()
    # report a message
    print(f'Worker is {process.name} with {value}', flush=True)
    # block for a moment
    sleep(1)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool(2, maxtasksperchild=3) as pool:
        # issue tasks to the process pool
        for i in range(10):
            pool.apply_async(task, args=(i,))
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()