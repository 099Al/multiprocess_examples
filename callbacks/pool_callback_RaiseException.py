# SuperFastPython.com
# example of determining what happens if an exception is raised in the result callback
from time import sleep
from multiprocessing.pool import Pool


# result callback function
def result_callback(result):
    print(f'Callback running.', flush=True)
    # failure
    raise Exception('Something bad happened')


# task executed in a worker process
def task(identifier):
    print(f'Task {identifier} done.', flush=True)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issue tasks to the process pool
        result = pool.map_async(task, range(5), callback=result_callback)
        # report tasks are issued
        print(f'Main tasks issued.', flush=True)
        # wait for tasks to complete
        result.wait()
        print(f'Main tasks done.', flush=True)
        # close the process pool
        pool.close()
        # wait for all tasks to complete
        pool.join()