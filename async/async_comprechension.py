# SuperFastPython.com
# example of an alternative to an await list comprehension
import asyncio


# task coroutine
async def task_coro(value):
    # block a moment to simulate work
    await asyncio.sleep(1)
    # calculate and return
    return value * 10

# define an asynchronous generator
async def async_generator():
    # normal loop
    for i in range(10):
        # block to simulate doing work
        await asyncio.sleep(1)
        # yield the result
        yield i

# main coroutine
async def main():
    # create a list of awaitables
    awaitables = [task_coro(i) for i in range(10)]
    # gather the awaitables concurrently
    results = await asyncio.gather(*awaitables)
    # report results
    print(results)

    # SuperFastPython.com
    # example of an await list comprehension
    import asyncio

# main coroutine
"""This process continues until all coroutines in the list of awaitables have been awaited.
The current coroutine will be suspended to execute awaitables sequentially, 
which is different and perhaps slower than executing them concurrently using asyncio.gather().

"""
async def main2():
    # create a list of awaitables
    awaitables = [task_coro(i) for i in range(10)]
    # await list comprehension to collect results
    results = [await a for a in awaitables]
    # report results
    print(results)




# main coroutine
async def main3():
    # asynchronous list comprehension
    results = [item async for item in async_generator()]
    # report results
    print(results)





# run the asyncio program
asyncio.run(main3())