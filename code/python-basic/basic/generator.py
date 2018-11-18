

g = (x * x for x in range(10))  # 创建生成器，节省空间
next(g) # 获取下一个值
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # yield 命令
        a, b = b, a + b
        n = n + 1
    return 'done'