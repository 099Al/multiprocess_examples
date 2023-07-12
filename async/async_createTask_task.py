"""
Create a Task with asyncio.create_task() (recommended)
Create a Task with asyncio.ensure_future() (low-level)
Create a Task with loop.create_task() (low-level)

"""

# SuperFastPython.com
# example of creating many tasks with asyncio.create_task()
import asyncio


# define a coroutine for a task
async def task_coroutine(number):
    # report a message
    print(f'>executing the task {number}')
    # block for a moment
    await asyncio.sleep(1)
    return 'hello'


# custom coroutine
async def main():
    # report a message
    print('main coroutine started')

    # create and schedule a task with a name
    #Вариант 1 запуска
    task = asyncio.create_task(task_coroutine(100), name='MyTask')
    res = await task     #awit не обязательно, без него тоже выполнится
    print(1,res)
    res2 = task.result()
    print(2,res2)

    #Вариант 2 запуска
    # create and schedule many tasks
    tasks = [asyncio.create_task(task_coroutine(i)) for i in range(20)]
    # wait for each task to complete
    for task in tasks:
        await task
    # report a final message
    print('main coroutine done')  #Выполняется после await. Без await выполниться сразу

    #Вариант 3 запуска
    #Вывод результат
    values = await asyncio.gather(task_coroutine(101), task_coroutine(102))
    print(values)

    #Вариант 4 запуска аналогичен варианту 3
    coros = [task_coroutine(101), task_coroutine(102), task_coroutine(103)]
    # execute all coroutines concurrently
    values = await asyncio.gather(*coros)
    print(3, values)



# start the asyncio program
asyncio.run(main())