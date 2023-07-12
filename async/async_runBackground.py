# SuperFastPython.com
# example of running an asyncio coroutine in the background
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
    # schedule the coroutine to run in the background

    task = asyncio.create_task(coro)
    await asyncio.sleep(0) #Для запуска task, созданного через asyncio.create_task

    # report a message
    print('Main doing other stuff...')
    # simulate continue on with other things
    await asyncio.sleep(5)


# run the asyncio program
asyncio.run(main())