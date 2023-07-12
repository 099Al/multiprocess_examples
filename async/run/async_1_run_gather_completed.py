import asyncio
import time
from aiohttp import ClientSession

#function with return
async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'APPID': '2a4ff86f9aaa70041ec8e82db64abf56'}

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            return f'{city}: {weather_json["weather"][0]["main"]}'


async def main(cities_):
    tasks = []
    for city in cities_:
        #tasks.append(asyncio.create_task(get_weather(city)))
        tasks.append(get_weather(city))  # Либо так
    #!!!!! #, asyncio.gather вернет список со значениями, которые вернули объекты.
    # Порядок значений в списке соответствует порядку объектов
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

    print('----2 variant--------')
    tasks = [get_weather(city) for city in cities_]
    #Порядок не сохраняется
    for t in asyncio.as_completed(tasks):
        res = await t
        print(res)




cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

if __name__ == '__main__':
    print(time.strftime('%X'))

    asyncio.run(main(cities))

    print(time.strftime('%X'))