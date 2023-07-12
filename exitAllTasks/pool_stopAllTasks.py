# SuperFastPython.com
# example of safely stopping all tasks in the process pool
from time import sleep
from multiprocessing import Event
from multiprocessing import Manager
from multiprocessing.pool import Pool


# task executed in a worker process
def task(identifier, event):
    print(f'Task {identifier} running', flush=True)
    # run for a long time
    for i in range(10):
        # block for a moment
        sleep(1)
        # check if the task should stop
        if event.is_set():
            print(f'Task {identifier} stopping...', flush=True)
            # stop the task
            break
    # report all done
    print(f'Task {identifier} Done', flush=True)


# protect the entry point
if __name__ == '__main__':
    # create the manager
    with Manager() as manager:
        # create the shared event
        event = manager.Event()
        # create and configure the process pool
        with Pool() as pool:
            # prepare arguments
            items = [(i, event) for i in range(4)]
            # issue tasks asynchronously
            result = pool.starmap_async(task, items)
            # wait a moment
            sleep(2)
            # safely stop the issued tasks
            print('Safely stopping all tasks')
            event.set()
            # wait for all tasks to stop
            result.wait()