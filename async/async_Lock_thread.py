# SuperFastPython.com
"""
A thread can only acquire a mutex lock once.
Attempting to acquire a lock that itself already holds, results in a deadlock.

example of a thread attempting to acquire the same lock more than once
"""
from threading import Thread
from threading import Lock


# function executed in a new thread
def task(lock):
    # report a message
    print('Acquiring lock')
    # acquire the lock
    with lock:
        # report a message
        print('Acquiring lock again')
        # acquire the lock
        with lock:
            # report message
            print('All done')


# create the lock
lock = Lock()
# create the thread
thread = Thread(target=task, args=(lock,))
# start the thread
thread.start()
# wait for the thread to finish
thread.join()