#!/usr/bin/python

import random
from multiprocessing import Pool, cpu_count
from math import sqrt
from timeit import default_timer as timer


def pi_part(n):
    #print(n)

    count = 0

    for i in range(int(n)):

        x, y = random.random(), random.random()

        r = sqrt(pow(x, 2) + pow(y, 2))

        if r < 1:
            count += 1

    return count


def main():

    start = timer()

    cpu_n = cpu_count()
    print(f'You have {cpu_n} cores')

    n = 1_000_000_000

    part_count = [n/cpu_n for i in range(cpu_n)]


    with Pool(processes=cpu_n) as pool:

        count = pool.map(pi_part, part_count)
        pi_est = sum(count) / (n * 1.0) * 4

        end = timer()

        print(f'elapsed time: {end - start}')
        print(f'π estimate: {pi_est}')

if __name__=='__main__':
    main()