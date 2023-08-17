## start from 0 lines of code to 10,000

import time
import threading
import multiprocessing


def incrementing(max):
    number = 0
    for i in range(max):
        number += 1
    print(number)

def incrementrange1(min,max):
    number = min
    for i in range(min,max):
        number += 1
    print("Done1")

def incrementrange2(min,max):
    number = min
    for i in range(min,max):
        number += 1
    print("Done2")

if __name__ == "__main__":
    # Specify the length
    number = 0
    split = 0
    max = 5e8

    start_time = time.time()
    incrementing(int(max))
    end_time = time.time()
    execution_time = end_time - start_time

    
    print( f" incrementing took {execution_time} seconds to execute ")

    start_time = time.time()
    split = int(max / 2)

    thread1 = threading.Thread(target=incrementrange1(0,split))
    thread2 = threading.Thread(target=incrementrange2(split,int(max)) )

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print( f" threading {execution_time} seconds to execute ")


    start_time = time.time()
    processes = []

    process1 = multiprocessing.Process(target=incrementrange1,args=(0,split))
    processes.append(process1)

    process2 = multiprocessing.Process(target=incrementrange1,args=(split,int(max)))
    processes.append(process2)

    process1.start()
    process2.start()
   

    for process in processes:
        process.join()

    end_time = time.time()
    execution_time = end_time - start_time

    print( f" multi processing {execution_time} seconds to execute ")