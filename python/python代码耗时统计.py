1.time.time()来计时
2.1 cProfile
  python -m cProfile myscript.py
2.2 cProfile包装
import cProfile
import pstats
from contextlib import contextmanager

@contextmanager
def profiling(sortby='cumulative',limit=20):
    pr = cProfile.Profile()
    pr.enable()
    yield
    pr.disable()
    ps = pstats.Stats(pr).sort_stats(sortby)
    ps.print_stats(limit)

with profiling(sortby='tottime',limit=10):
    # execute code

3. Line Profiler ： 告诉你一个函数中每一行的耗时
from line_profiler import LineProfiler
import random

def do_stuff(numbers):
    s = sum(numbers)
    l = [numbers[i]/43 for i in range(len(numbers))]
    m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

numbers = [random.randint(1,100) for i in range(1000)]
lp = LineProfiler()
lp_wrapper = lp(do_stuff)
lp_wrapper(numbers)
lp.print_stats()
