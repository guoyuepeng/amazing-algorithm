# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

import functools

def log(func):
    @functools.wraps(func)    # 需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
@log   # 相当于 now = log(now)
def now():
    print('2015-3-25')
now()

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
