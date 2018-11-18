# coding: utf-8
# pdb #

command = {'break/b 行号/函数名': '设置断点', 'continue/c': '继续执行程序', 'list/l': '查看当前的代码段', 'step/s': '进入函数',
           'return/r': '执行代码直到从当前函数返回', 'exit': '终止并退出', 'q': '终止并重启', 'next/n': '执行下一行', 'pp 变量名': '打印变量的值',
           'help': '帮助', 'args/a': '打印当前函数的参数', 'jump/j': '让程序跳到指定行'}

# 开启pdb调式的方法
# 1. 命令行
# python -m pdb test.py   ## 断点就是程序执行的第一行

# 2. python中调试
import pdb

pdb.run('modulename.test()')

# 3. 插入断点
import pdb

pdb.set_trace()

# example ############
# 1
import pdb

a = "aaa"
pdb.set_trace()  # 脚本直接运行会停止在下一行
b = "bbb"
c = "ccc"
final = a + b + c
print(final)

# pycharm自带debug ################
# http://blog.csdn.net/u013088062/article/details/50130991
# 右上角 绿色“debug”
# 设置断点
# debugger窗口：显示当前运行的进程，查看变量
# Console窗口：查看程序给出的错误信息，并增加额外运算（打开“Show Command Line”）
