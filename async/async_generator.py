# SuperFastPython.com
# example of asynchronous generator with async for loop
import asyncio


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
    # loop over async generator with async for loop
    async for item in async_generator():
        print(item)

# main coroutine
async def main2():
    # create the async generator
    gen = async_generator()
    # step the generator one iteration
    awaitable = anext(gen)
    # get the result from one iteration
    result = await awaitable
    # report the result
    print(result)

# main coroutine
async def main3():
    # loop over async generator with async for loop
    async for item in async_generator():
        print(item)

# main coroutine
async def main4():
    # loop over async generator with async comprehension
    results = [item async for item in async_generator()]
    # report results
    print(results)


# execute the asyncio program
asyncio.run(main4())