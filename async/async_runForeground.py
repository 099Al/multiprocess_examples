# SuperFastPython.com
# example of running an asyncio coroutine in the foreground
import asyncio


# custom coroutine
async def custom_coro():
    # report a message
    print('Coroutine is running')
    # simulate some long running task
    await asyncio.sleep(5)
    # report another message
    print('Coroutine is done')


# main coroutine
async def main():
    # create the coroutine
    coro = custom_coro()
    # run the coroutine in the foreground
    await coro


# run the asyncio program
asyncio.run(main())