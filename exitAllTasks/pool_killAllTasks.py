# SuperFastPython.com
# example of killing all tasks in the process pool
from time import sleep
from multiprocessing.pool import Pool


# task executed in a worker process
def task(identifier):
    print(f'Task {identifier} running', flush=True)
    # run for a long time
    for i in range(10):
        # block for a moment
        sleep(1)
        print(f"{identifier} val:{i}")
    # report all done
    print(f'Task {identifier} Done', flush=True)


# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        # issues tasks to process pool
        _ = pool.map_async(task, range(4))
        # wait a moment
        sleep(5)
        # kill all tasks
        print('Killing all tasks')
        pool.terminate()
        # wait for the pool to close down
        pool.join()