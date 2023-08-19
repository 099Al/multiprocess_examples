import httpx
import asyncio
import random


async def http_req(ref):
    async with httpx.AsyncClient() as client:
        v = random.randint(1,5)
        await asyncio.sleep(v)
        try:
            r = await client.get(ref)
        except:
            r = 'Error'
        #print('f',r,v)  #Выведется что быстрее отработает
        return r,v


async def many_req():
    l = ['https://www.google2.com/','https://www.example.com/','https://www.google.com/']
    tasks = [http_req(x) for x in l]
    res = await asyncio.gather(*tasks)

    #Вывод будет в том порядке как были поданы переменные
    for r in res:
        print(r)

    print('----')
    tasks = [http_req(x) for x in l]
    for r in asyncio.as_completed(tasks):
        res = await r
        print(res)


if __name__ == '__main__':

        asyncio.run(many_req())
        #print(res)

