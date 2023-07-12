# SuperFastPython.com
# example of wait/notify with an asyncio condition
import asyncio


# task coroutine
async def task(condition, work_list):
    # block for a moment
    await asyncio.sleep(5)
    # add data to the work list
    work_list.append(33)
    # notify a waiting coroutine that the work is done
    print('Task sending notification...')
    async with condition:       #без этого условия asyncio.create_task не поймет, что функция завершилась. К след шагу не перейдет
        condition.notify()


    # main coroutine
async def main():
    # create a condition
    condition = asyncio.Condition()
    # prepare the work list
    work_list = list()
    # wait to be notified that the data is ready
    print('Main waiting for data...')
    async with condition:
        # create and start the a task
        _ = asyncio.create_task(task(condition, work_list))
        # wait to be notified
        print('--1--')
        await condition.wait()  #Ожидание notyfy, чтобы перейти к след шагу
        print('--2--')
    # we know the data is ready
    print(f'Got data: {work_list}')


# run the asyncio program
asyncio.run(main())