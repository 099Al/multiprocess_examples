# SuperFastPython.com
# demonstration with the process pool life-cycle

"""
future ожидает выполнение таска
и через нее можно получить результат, который возвращается через return
"""

from time import sleep
from concurrent.futures import ProcessPoolExecutor


# a simple task that blocks for a moment and prints a message
def task():
    # block for a moment
    sleep(1)
    # display a message
    print(f'Task running in a worker process')
    # return a message
    return 'All done'


# entry point
if __name__ == '__main__':
    # create the pool of worker processes
    with ProcessPoolExecutor() as executor:
        # execute a task in another process
        future = executor.submit(task)
        # display a message
        print('Waiting for the new process to finish...')
        # wait for the task to finish and get the result
        result = future.result()
        # report the result
        print('res',result)
    # shutdown the process pool automatically