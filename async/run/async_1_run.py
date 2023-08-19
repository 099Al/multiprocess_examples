import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(5)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    #Функции отрабатывают в произвольном порядке(в зависимости от времени ожидания в sleep)
    task1 = asyncio.create_task(fun1(4)) #Функция начинает работать на этом шаге
    task2 = asyncio.create_task(fun2(4))


    await task1  #работает дольше. task1 ставит в ожидание, но task2 отрабатывает раньше
    await task2  # ждем task2, но из-за task1 он уже отработал в данный момент

    """
    ждем task2 он отрабатывает раньше
    затем срабатывает print
    затем ждем task1
    """
    #await task2
    #print('1')
    #await task1

    #!!! Если await не прописывать, то task1 и task2 отработают, но задержки  не будет


print(time.strftime('%X'))

#Новый вариант
if __name__ == '__main__':
    asyncio.run(main())

    #Старый вариант
    '''
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(fun1(4))
    task2 = loop.create_task(fun2(4))
    loop.run_until_complete(asyncio.wait([task1, task2]))
    '''

    print(time.strftime('%X'))