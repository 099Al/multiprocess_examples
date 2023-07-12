# SuperFastPython.com
# example of a done callback function for a future from gather()
import asyncio


# define a custom callback function
def handler(future):
    # get all results
    results = future.result()
    # process all results
    for result in results:
        print(f'>got {result}')


# coroutine used for a task
async def task_coro(value):
    # sleep for a moment
    await asyncio.sleep(1)
    # return a custom value
    return value * 10


# coroutine used for the entry point
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # execute all coroutines as a group
    future = asyncio.gather(*coros)
    # add the done callback function
    future.add_done_callback(handler)
    # continue on with other things...
    await asyncio.sleep(2)


# start the asyncio program
asyncio.run(main())