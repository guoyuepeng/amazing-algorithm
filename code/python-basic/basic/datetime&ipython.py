##################### datetime  ######################
########### function: handing date and time ##########
######################################################
# 数据类型
# date：存储日历日期(年月日)
# time：将时间存储为时、分、秒、毫秒
# datetime：存储日期和时间
# timedelta:两个datetime之间的差

# get current date&time
from datetime import datetime

now = datetime.now()
print(now)  ## type:datetime
now.year, now.month, now.day, now.date()

# get specific date&time
dt = datetime(2016, 4, 19, 12, 20)

# convert datetime to timestamp
# timestamp:相对于epoch time(1970.1.1 00:00:00)的秒数,irrelevant with time zone
dt.timestamp()  # 小数表示毫秒

# convert timestamp to datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))

# convert str to datetime
cday = datetime.strptime('2015-06-01 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)  # dateutil:不需要编写格式定义(实用但不完美,会误解析)
from dateutil.parser import parser

parser('2011-01-03')
parser('Jan 31,1997 10:45 PM')
parser('6/12/2011', dayfirst=True)  # 如果日出现的月的前面
# pd.to_datetime:解析多种不同的日期表示形式
datestrs = ['7/6/2011', '8/6/2011']
pd.to_datetime(datestrs)  # NaT:时间戳数据的NA值

# convert datetime to str
str(now)
print(now.strftime('%a,%b %d %H:%M'))

# add/minus datetime
from datetime import timedelta

now = datetime.now()
now + timedelta(hours=10)
now + timedelta(days=1)



##################### ipython  ######################
########### function: interactive command shell ##########
######################################################
# # Tab ：补全
# # ? ：显示对象的通用信息,搜索命名空间
# np. * laod *?
# # ?? : 显示源代码
# # 　%run：运行脚本
# # ctrl-c：中断执行代码
# # 　%paste：整体粘贴
# # %time:python语句执行时间(执行一次)
# # %timeit:python语句执行时间(自动执行多次，求平均时间)
# # 最近的两个输出结果保存在_,__变量中
# # %logstar:开启记录日志
# # 交互式调试器：%pdb
# # 基本性能分析：cProfile模块
# # shell：
# python - m
# cProfie - s
# cumulative
# test.py  # 输出各函数执行时间,-s cumulative:输出结果按时间排序
# # ipython:
# % prun - 1
# 7 - s
# cumulative
# run_experiment()  # 分析python语句执行时间
# % run - p - s
# cumulative
# test.py
# # line_profiler模块：逐行分析
# % lprun - f
# func1
# statement_to_profile  # 需要指定函数:func1  # 重新加载模块
# reload(some_lib)
# # 实在不行，重启ipython
# # 代码设计
# # 扁平结构要比嵌套结构好


######### time series #########
# TimeSeries：带有DatetimeIndex的Series
# 时间戳存储格式：datetime64
import pandas as pd
pd.date_range(start='1/1/2000', end, periods=1000, freq, normalize)  # normalize=True：将日期格式规整化
# freq:每日/每小时/每秒/每月最后一个工作日/每个月第n个星期几
# 索引：可以按数字,日期(具体日期,年,年月),
# 索引是否唯一
df.index.is_unique
# 聚合
df.groupby(level=0)

# 将时间序列转换为固定频率
ts.resample('D')  # 每日



##################### pymssql  ######################
########### function: remote data access ##########
######################################################

import pymssql,pymysql

conn = pymssql.connect(**finfdb_dev)
cursor = conn.cursor()
cursor.execute("""
delete from finf_stmt_is_indu
where CREATE_BY='algorithm_datayes'
""")
conn.commit()
conn.close()


# read data from database
data_apidb_conn1 = pymysql.connect(**data_apidb)
pd.read_sql("select * from table ", data_apidb_conn1)


