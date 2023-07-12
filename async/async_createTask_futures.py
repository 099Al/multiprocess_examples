# SuperFastPython.com
# example of creating a task with asyncio.ensure_future()

"""
The asyncio.ensure_future() allows the caller to
specify the event loop used to schedule the task via the “loop” argument.
By default, it will use the current event loop
that is executing the coroutine that is creating the task.

"""
import asyncio


# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)


# custom coroutine
async def main():
    # report a message
    print('main coroutine started')
    # create and schedule the task
    task = asyncio.ensure_future(task_coroutine())
    # wait for the task to complete
    await task
    # report a final message
    print('main coroutine done')


# start the asyncio program
asyncio.run(main())