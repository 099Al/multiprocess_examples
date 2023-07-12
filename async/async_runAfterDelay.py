# SuperFastPython.com
# example of starting a coroutine after a delay
import asyncio


# coroutine that will start another coroutine after a delay in seconds
async def delay(coro, seconds):
    # suspend for a time limit in seconds
    await asyncio.sleep(seconds)
    # execute the other coroutine
    await coro


# task coroutine to do something
async def task_coro():
    # report a message
    print('Coroutine is running')
    # simulate some long running task
    await asyncio.sleep(3)
    # report another message
    print('Coroutine is done')


# main coroutine
async def main():
    # report a message
    print('Main starting the delay')

    # Первый вариант запуска
    await delay(task_coro(), 3)


    #Второй вариант
    task = asyncio.create_task(delay(task_coro(), 3))
    await asyncio.sleep(0)  #Для запуска task, созданного через asyncio.create_task

    # simulate doing other things...
    await asyncio.sleep(7)

    # report a final message
    print('Main all done')


# run the asyncio program
asyncio.run(main())