# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df.dropna(axis=0, how='any'))   # how={'any', 'all'}
print(df.fillna(value=0)) # method = ffill,bfill
print(pd.isnull(df))


df.isnull().sum()  # 查每一列有多少个NAN值
df[df.isnull().any(axis=1)] # 找到NAN值
df = df[np.isfinite(df[colname])] # 丢掉含有NAN值的指定列