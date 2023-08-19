# example of using asyncio.Runner
from asyncio import Runner
from asyncio import sleep


# example coroutine
async def task_coro1():
    print('Hello from first coro')
    await sleep(1)


# another example coroutine
async def task_coro2():
    print('Hello from second coro')
    await sleep(1)

if __name__ == '__main__':

    # entry point of the program
    """
    Чтобы заменить такой запуск:
    # asyncio entry point
    async def main():
        # execute the first coroutine
        await task_coro1()
        # execute the second coroutine
        await task_coro2()
     
    # entry point of the program
    run(main())
    """

    with Runner() as runner:
        # execute the first coroutine
        runner.run(task_coro1())
        # execute the second coroutine
        runner.run(task_coro2())

