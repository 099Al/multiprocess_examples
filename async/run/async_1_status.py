"""
# get a set of all running tasks
all_tasks = asyncio.all_tasks()

# get the current tasks
current_task = asyncio.current_task()

# remove the current task from the list of all tasks
all_tasks.remove(current_task)

# suspend until all tasks are completed
await asyncio.wait(all_tasks)

"""

import asyncio


# define a main coroutine
async def main():
    # report a message
    print('main coroutine started')
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(task)

if __name__ == '__main__':
    # start the asyncio program
    asyncio.run(main())