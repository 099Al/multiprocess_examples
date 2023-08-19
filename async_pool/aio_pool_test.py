import asyncio

from .aio_pool.pool import AioPool

async def powlong(a):
  await asyncio.sleep(1)
  return a**2

if __name__ == '__main__':
  with AioPool(processes=2, concurrency_limit=8) as pool:
    results = pool.map(powlong, [i for i in range(16)])  # Should take 2 seconds (2*8).
    print(results)