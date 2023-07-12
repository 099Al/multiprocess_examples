import asyncio
import random
import time
import datetime



async def test_connect(p):
    t = random.randint(1,5)
    await asyncio.sleep(t)  #если использовать time.sleep(), то будет последовательное выполнение
    return t

async def scan(nm):
    print(f'start n:{nm}')


    res = await test_connect(nm)
    print(f'end n:{nm} wait:{res}')

async def main():

    tasks = [scan(x) for x in l_rn]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    print('---start--')


    l_rn = range(0,5)

    start_tm = datetime.datetime.now()

    asyncio.run(main())

    end_tm = datetime.datetime.now()

    print('total:',end_tm-start_tm)

    #test_connect('a')



    print('---end---')