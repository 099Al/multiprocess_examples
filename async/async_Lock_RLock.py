# SuperFastPython.com
# example of using a threading RLock in an asyncio program
from random import random
from threading import RLock
import asyncio


# task coroutine with a critical section
async def task(lock, num, value):
    # acquire the lock to protect the critical section
    with lock:
        # report a message
        print(f'>coroutine {num} got the lock, sleeping for {value}')
        # block for a moment
        await asyncio.sleep(value)


# entry point
async def main():
    # create a shared lock
    lock = RLock()
    # create many concurrent coroutines
    coros = [task(lock, i, random()) for i in range(10)]
    # execute and wait for tasks to complete
    await asyncio.gather(*coros)

# run the asyncio program