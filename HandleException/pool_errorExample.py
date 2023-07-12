"""
This highlights that we cannot pass a process pool instance directly to child worker processes in the process pool.

pool objects cannot be passed between processes or pickled
"""
# example of attempting to share the pool with a worker process
from multiprocessing.pool import Pool


# error callback function
def handler(error):
    print(error, flush=True)


# task executed in a worker process
def task(pool):
    # report a message
    print(f'Pool Details: {pool}', flush=True)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue a task to the process pool
        pool.apply_async(task, args=(pool,), error_callback=handler)
        # close the pool
        pool.close()
        # wait for all issued tasks to complete
        pool.join()