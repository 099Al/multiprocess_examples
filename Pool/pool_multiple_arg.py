import multiprocessing

from functools import partial

data_list = [1, 2, 3, 4]



def prod_xy(x,y):

    return x * y



def parallel_runs(data_list):

    pool = multiprocessing.Pool(processes=4)

    prod_x=partial(prod_xy, y=10) # prod_x has only one argument x (y is fixed to 10)

    result_list = pool.map(prod_x, data_list)

    print(result_list)



if __name__ == '__main__':

    parallel_runs(data_list)