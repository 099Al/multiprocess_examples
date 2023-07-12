# SuperFastPython.com
# example of checking changing the start method used in the process pool
from multiprocessing.pool import Pool
from multiprocessing import get_start_method
from multiprocessing import get_context


# task executed in a worker process
def task():
    # get the start method
    method = get_start_method()
    # report a message
    print(f'Worker using {method}', flush=True)


# protect the entry point
if __name__ == '__main__':
    # get the start method
    method = get_start_method()
    print(f'Main process using {method}')
    # create a process context
    ctx = get_context('fork')
    # create and configure the process pool
    with Pool(context=ctx) as pool:
        # issue tasks to the process pool
        pool.apply_async(task)
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()