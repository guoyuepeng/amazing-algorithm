# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib

## python启动路径，package搜索路径
## python启动路径：PATH里面最后一个路径
## package搜索路径： PYTHONPATH
## 命令窗口添加
export PATH=$PATH:<你的要加入的路径>
## python脚本中添加
import sys
sys.path.append(你的要加入的路径)
## 跑python script前添加搜索路径
PYTHONPATH=newpath python somescript.py somecommand


## ipython notebook --port=9001 --no-browser --ip=*
## 端口：9001 9002 8889 9999 10000 10001......
## ipython notebook 快捷键调出：ctrl+M +H

## 添加module路径  sys.path.append()
## 查看安装的包：
help('modules')
np.__version__  # 检查package版本

df= pd.DataFrame()

df.replace([],[]) # dataframe内容替换

df.columns.str.replace("date", "datetime")  # 更改列名
df = df.rename(columns={'$a': 'a', '$b': 'b'})


df.groupby(['columns1','columns2'],as_index=False) # 聚合

# 对DataFrame字符串作操作
df['year']=df['effectdate'].str.split('-').str.get(0)
# 转换为日期格式
df['column_name']=pd.to_datetime(df.column_name.values)

dir() # 查看现有变量

df.reset_index(inplace=True) # multiindex 转换成 columns

average(a, weights=[1,2]) # 加权平均

pd.cut(array,bins) # 数据离散化

# 全展示
from IPython.core.display import HTML
HTML(df.to_html())


int(''.join(x for x in example if x.isdigit())) # 取出example里面的数字
(''.join(x for x in example if x.alpha()))  # 取出example里面的字母

np.where() # 强大的赋值函数

## matplotlib 画中文label
# 最简单的方法是修改配置文件
matplotlib.matplotlib_fname() # 会显示matplotlibrc文件的地址
# 修改matplotlibrc文件
# 将文件中的
    #font.family: sans-serif
# 去掉注释，修改为
    #font.family: Microsoft YaHei

%matplotlib inline
# fig, axs = plt.subplots()
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"/home/songwq/STZHONGS.TTF", size=14)
plt.xlabel('x轴名称',fontproperties=font,size=30)


# 计算前后两行百分数变化
df.pct_change()

# 代码计时：
import datetime
starttime = datetime.datetime.now()
#long running
endtime = datetime.datetime.now()
print ((endtime - starttime).seconds)

# 代码性能分析
import cProfile
cProfile.run('your_method()')


#运行.py文件输出错误：python file.py>file.log 2>&1

# python定时job
from apscheduler.schedulers.blocking import BlockingScheduler
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=ConstCfg.start_hour, minute=ConstCfg.start_minute,
                     misfire_grace_time=1000)

def main():
    if    # 作一些条件判断
    sched.start()
    retutn


# python运行shell脚本
import subprocess
subprocess.call(['./test.sh'])


# 转html
mpld3.save_html(fig,fileobj='test.html')

# function <apply> is slow

# dataframe占用空间
df.info(memory_usage='deep')
df.values.nbytes + df.index.nbytes + df.columns.nbytes # bytes
df.memory_usage() #Dataframe占用内存大小
