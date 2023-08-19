import time





if __name__ == '__main__':
    n=0
    while True:

        time.sleep(1)
        n=n+1
        print('a',n)

        k=0
        while True:

            try:
               k=k+1
               time.sleep(1)

               print('b',n,'---',k)
               if k==5:
                   raise Exception("inner loop")

            except Exception as e:
                print('error:',e )

