import asyncio

"""
Корутины регистрируются в event loop.
Затем проверяется по циклу готовность результата
Если результат готов, то функция выполняется.
После отработки всех функции в even loop идет переход к след шагу ???

all_tasks = asyncio.all_tasks()  #Получение списка тасков

"""

#----Пример--1----
# custom coroutine
async def custom_coro(message):
    # report the message
    print(message)


#----Пример--2----
# another custom coroutine
async def new_coro(message):
    # report the message
    print(message)


# custom coroutine
async def custom_coro2(message):
    # execute the new coroutine
    await asyncio.sleep(1)  #Тормозит выполнение след шагов
    await new_coro('Hi from coroutine within a coroutine 2')
    # report the message
    print(message)


#----Пример---3----

async def new_coro3(message):
    # report the message
    await asyncio.sleep(3)
    print(message)

async def custom_coro3(message):
    # create the new coroutine
    coro = new_coro3('Hi from coroutine within a coroutine 3')
    # wrap the coroutine in a task and schedule for execution

    #----вариант 1-------
    task = asyncio.create_task(coro)
    # wait for the task to complete
    await task  #!!! Если await не прописывать, то task отработает, но задержки  не будет
    #--------------------

    #----вариант 2 --------
    #await coro

    #----------------------

    # report the message
    print(message)


if __name__ == '__main__':

    #Запуск коорутины
    print(1)
    asyncio.run(custom_coro('Hi from a coroutine'))
    print(2)
    #----------------
    print(3)
    # await запускает коорутину только внутри функции
    asyncio.run(custom_coro2('Hi from a coroutine 2'))
    print(4)
    #----------------
    # create and execute coroutine
    asyncio.run(custom_coro3('Hi from a coroutine 3'))
    #all_tasks = asyncio.all_tasks()
    print(5)



