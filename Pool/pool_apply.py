import multiprocessing
from multiprocessing import Pool


def cube(x):
    return x**3


if __name__ == "__main__":
    print(multiprocessing.cpu_count())
    pool = Pool(processes=4)  # создаем пул из 4 процессов
    # в apply можно передать несколько аргументов
    results = [pool.apply(cube, args=(x,)) for x in range(1,7)]  # раскидываем числа от 1 до 7 по 4 процессам
    print(results)

    pool = Pool(processes=4)
    # то же самое, но с map. разбивает итерируемый объект (range(1,7)) на chunks и раскидывает аргументы по процессам
    results = pool.map(cube, range(1,7))
    print(results)