#-*-coding:utf-8-*-
# 多进程,多线程
# numpy
# numba

######### 多进程 ######### 
# 模块：multiprocessing
# 类：Pool

from multiprocessing import Pool
p_pool = Pool(processes=4)
rb_hfre_result = []
for ticker in ticker_list:
	rb_hfre_result.append(p_pool.apply_async(run_unit, args=(ticker, db, freq, cfg_filepath)))
p_pool.close()
p_pool.join()

# 进程（processes）的数量取决于任务是cpu密集还是io密集，如果是cpu密集，cpu已经loading已经很高，进程数量应该小于等于cpu core的数量

# cpu密集：计算密集型，指的是系统的硬盘、内存性能相对CPU要好很多，此时，系统运作大部分的状况是CPU Loading 100%，CPU要读/写I/O(硬盘/内存)，I/O在很短的时间就可以完成，而CPU还有许多运算要处理，CPU Loading很高。
# io密集：系统的CPU性能相对硬盘、内存要好很多，此时，系统运作，大部分的状况是CPU在等I/O (硬盘/内存) 的读/写操作，此时CPU Loading并不高。

# 计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，
# 但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。
# 计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，
# 最好用C语言编写。

# 第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成
# （因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。
# IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。
# 对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

# 总之，计算密集型程序适合C语言多线程，I/O密集型适合脚本语言开发的多线程。


# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
# 所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# 所以需要加锁


#########  多线程 ######### 
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)


# （1）引入threadpool模块
# （2）定义线程函数   
# （3）创建线程 池threadpool.ThreadPool()   
# （4）创建需要线程池处理的任务即threadpool.makeRequests()   
# （5）将创建的多个任务put到线程池中,threadpool.putRequest   
# （6）等到所有任务处理完毕theadpool.pool()

import time
import threadpool  
def sayhello(str):
    print "Hello ",str
    time.sleep(2)

name_list =['xiaozi','aa','bb','cc']
start_time = time.time()
pool = threadpool.ThreadPool(10) 
requests = threadpool.makeRequests(sayhello, name_list) 
[pool.putRequest(req) for req in requests] 
pool.wait() 
print '%d second'% (time.time()-start_time)


######### numba #########
# 在jit装饰器装饰的函数中，不可以有第三方的package
import time
import pandas as pd
from numba import jit
 
@jit
def time_com(i):
    cum = 0
    for test in range(i):
        for ind in range(i):
            cum += (test * ind) % 3
 
if __name__ == '__main__':
    t1 = time.clock()
    df = pd.DataFrame()
    for i in range(500):
        time_com(i)
    t2 = time.clock()
    print "run time:%f s" % (t2 - t1)





