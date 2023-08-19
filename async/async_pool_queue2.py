import asyncio
import random


async def wrapper(id_, queue, coroutine):
    await queue.put((id_, f'task {id_:2} completed after {await coroutine}'))


async def some_task():
    delay = random.uniform(0.5, 2)
    await asyncio.sleep(delay)
    return delay


async def stop_event_delayed(event: asyncio.Event):
    # insert stop value after 10 seconds
    await asyncio.sleep(6)
    print("Sending Stop signal!")
    event.set()


async def wait_until_val(queue: asyncio.Queue, end_val, callback):

    while (val := await queue.get()) is not end_val:
        queue.task_done()
        await callback(*val)

    queue.task_done()
    print("Received sentinel!")


def any_task_alive(task_list) -> bool:
    return any(not task.done() for task in task_list)


async def task_manager(pool_size):
    result_queue = asyncio.Queue()
    stop_event = asyncio.Event()

    # initialize pool with tasks
    pool = [asyncio.create_task(wrapper(idx, result_queue, some_task())) for idx in range(pool_size)]

    async def add_task_callback(idx, msg):
        # change task if event is not set
        if not stop_event.is_set():
            pool[idx] = asyncio.create_task(wrapper(idx, result_queue, some_task()))
        print(msg)
        # do some 'async' works here.

    # wait 10 secs before sending sentinel. Non-blocking, next line will run immediately.
    asyncio.create_task(stop_event_delayed(stop_event))

    # run consumer task to fetch and process tasks.
    consumer = asyncio.create_task(wait_until_val(result_queue, None, add_task_callback))

    # now wait until event, then put sentinel to stop replacing tasks.
    await stop_event.wait()
    await result_queue.put(None)

    # wait until sentinel is processed.
    await consumer


asyncio.run(task_manager(5))