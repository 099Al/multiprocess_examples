# SuperFastPython.com
# example of an asynchronous iterator with async comprehension
import asyncio


# define an asynchronous iterator
class AsyncIterator():
    # constructor, define some state
    def __init__(self):
        self.counter = 0

    # create an instance of the iterator
    def __aiter__(self):
        return self

    # return the next awaitable
    async def __anext__(self):
        # check for no further items
        if self.counter >= 10:
            raise StopAsyncIteration
        # increment the counter
        self.counter += 1
        # simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter


# main coroutine
async def main():
    # loop over async iterator with async comprehension
    results = [item async for item in AsyncIterator()]
    # report results
    print(results)

# main coroutine
async def main2():
    # loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(item)

# main coroutine
async def main3():
    # create the async iterator
    it = AsyncIterator()
    # step the iterator one iteration
    awaitable = anext(it)
    # get the result from one iteration
    result = await awaitable
    # report the result
    print(result)

# execute the asyncio program
asyncio.run(main3())