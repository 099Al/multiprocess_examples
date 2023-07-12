# SuperFastPython.com
# example of an asyncio concurrent port scanner that limits concurrent connections
import asyncio


# returns True if a connection can be made, False otherwise
async def test_port_number(host, port, timeout=3):
    # create coroutine for opening a connection
    coro = asyncio.open_connection(host, port)
    # execute the coroutine with a timeout
    try:
        # open the connection and wait for a moment
        _, writer = await asyncio.wait_for(coro, timeout)
        # close connection once opened
        writer.close()
        # indicate the connection can be opened
        return True
    except asyncio.TimeoutError:
        # indicate the connection cannot be opened
        return False


# coroutine to scan ports as fast as possible
async def scanner(host, task_queue):
    # read tasks forever
    while True:
        # read one task from the queue
        port = await task_queue.get()
        # check for a request to stop scanning
        if port is None:
            # add it back for the other scanners
            await task_queue.put(port)
            # stop scanning
            break
        # scan the port
        if await test_port_number(host, port):
            # report the report if open
            print(f'> {host}:{port} [OPEN]')
        # mark the item as processed
        task_queue.task_done()
        """
        Finally, once the port number has been processed, we can mark it as such using the task_done() method.
        This will be needed later when the main() coroutine needs to know that all port numbers have been processed.
        """


# main coroutine
async def main(host, ports, limit=100):
    # report a status message
    print(f'Scanning {host}...')
    # create the task queue
    task_queue = asyncio.Queue()
    # start the port scanning coroutines
    workers = [asyncio.create_task(scanner(host, task_queue)) for _ in range(limit)]  #Запускается конечное кол-во workers. Каждый Worker берет задаиние из queue

    # issue tasks as fast as possible  #Добавление ports в очередь
    for port in ports:
        # add task to scan this port
        await task_queue.put(port)
    # wait for all tasks to be complete
    await task_queue.join()

    #Сигнал на остановку очереди, после того, как все элементы в очереди отработали. После .join()
    # signal no further tasks
    await task_queue.put(None)


# define a host and ports to scan
host = 'python.org'
ports = range(1, 1024)
# start the asyncio program
asyncio.run(main(host, ports))