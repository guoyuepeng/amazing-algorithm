# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

import multiprocessing as mp
import time

def job(v, num, l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    l.release()

def multicore():
    l = mp.Lock()           # 在多进程使用共享内存时，不同进程不互相干扰
    v = mp.Value('i', 0)    # 多进程之间变量共享只能用共享内存的方式
                            # i : 参数类型int，https://docs.python.org/3/library/array.html
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

def shared_memory():
    # 多进程之间变量共享只能用共享内存的方式
    value1 = mp.Value('i', 0)   # i : 参数类型int，https://docs.python.org/3/library/array.html
    value2 = mp.Value('d', 3.14)
    array = mp.Array('i', [1, 2, 3, 4])  # 这里的Array和numpy中的不同，它只能是一维的，不能是多维的

if __name__ == '__main__':
    multicore()



