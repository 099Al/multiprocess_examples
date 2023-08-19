# SuperFastPython.com
# example of stopping all running tasks when one task fails
from time import sleep
from multiprocessing import Manager
from multiprocessing import Event
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait
from concurrent.futures import FIRST_EXCEPTION


# target task function
def work(event, name):
    # pretend read src_data for a long time
    for _ in range(10):
        # pretend to read some src_data
        sleep(1)
        # check if this task should fail
        if name == 0:
            print(f'Task has failed, name={name}', flush=True)
            raise Exception('Something bad happened')
        # check if the task should stop
        if event.is_set():
            print(f'Stopping, name={name}', flush=True)
            return


# entry point
if __name__ == '__main__':
    # create a manager for sharing events
    with Manager() as manager:
        # create an event used to stop running tasks
        event = manager.Event()
        # create a process pool
        with ProcessPoolExecutor(10) as executor:
            # execute many tasks
            futures = [executor.submit(work, event, i) for i in range(10)]
            # wait for all tasks to complete, or one task to fail
            print('Waiting for tasks to complete, or fail...')
            done, not_done = wait(futures, return_when=FIRST_EXCEPTION)
            # check if not all tasks are done
            if len(done) > 0 and len(done) != len(futures):
                # check if an exception was raised
                future = done.pop()
                if future.exception() != None:
                    print(f'One task failed with: {future.exception()}, shutting down')
                    # cancel any scheduled tasks
                    for future in futures:
                        future.cancel()
                    # stop all running tasks
                    event.set()
    print('All done.')