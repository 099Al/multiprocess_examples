import asyncio
from aio_pool.pool import AioPool
from multiprocessing import current_process
from asyncio import current_task
import datetime
import random


async def powlong(a):

  process = current_process().name
  pid = current_process().pid
  task = current_task().get_name()
  start = datetime.datetime.now()
  print(f'{process},{a},{task} {pid}')

  t = random.randint(1,7)
  await asyncio.sleep(1)

  end = datetime.datetime.now()
  print(f'{process},{a},{task} {start} {end}  {(end-start).total_seconds()}')

  return a**2

if __name__ == '__main__':
  start = datetime.datetime.now()
  print(current_process().pid)

  with AioPool(processes=4, concurrency_limit=6) as pool:
    results = pool.map(powlong, [i for i in range(24)])  # Should take 2 seconds (2*8).
    print(results)

  end = datetime.datetime.now()

  print(end-start)