import asyncio
from datetime import datetime

async def print_number(task_name):
    print(f">>> Start {task_name}")
    for _ in range(5):
        print(42)
        await asyncio.sleep(0.5)
    print(f"<<< End {task_name}")


async def print_text(task_name):
    print(f">>> Start {task_name}")
    for _ in range(5):
        print("hello")
        await asyncio.sleep(0.9)
    print(f"<<< End {task_name}")

async def main():
    print(f'Start {datetime.now()}')


    #--1й способ--функции запускаются параллельно из-зи create_task
    task1 = asyncio.create_task(print_number('task1'))
    task2 = asyncio.create_task(print_text('task2'))
    await task1
    await task2


    #--2й способ-- функциии отрабатывают последовательно
    # await print_number(1)
    # await print_text('a')

    print(f'End {datetime.now()}')


if __name__ == '__main__':
    asyncio.run(main())
