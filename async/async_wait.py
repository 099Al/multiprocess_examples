# SuperFastPython.com
# example of waiting for all tasks to complete
from random import random
import asyncio


# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')


# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks) # Можно заменить на   results = await asyncio.gather(*tasks)

    """
    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    
    # wait for the first task to be completed
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    # wait for the first task to fail
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    
    # wait for all tasks to complete with a timeout
    done, pending = await asyncio.wait(tasks, timeout=3)
    """
    # report results
    print('All done')

# wait for all tasks to complete
done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

# start the asyncio program
asyncio.run(main())