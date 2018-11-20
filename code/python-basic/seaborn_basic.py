# Matplotlib试着让简单的事情更加简单，困难的事情变得可能，而Seaborn就是让困难的东西更加简单。
# 用Matplotlib最大的困难是其默认的各种参数，而Seaborn则完全避免了这一问题。

# sns 画热力图
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import mpld3
import numpy as np
import pandas as pd
font = FontProperties(fname=r"D:\materials\code\python\STZHONGS.TTF", size=14)
plt.switch_backend('agg')
fig,ax= plt.subplots()
index_return = index_return[index_return.columns].astype(float)
sns.set(font=font.get_name())
sns.heatmap(index_return,annot=True, fmt='.2%', center=0.1)
plt.ylabel('Step', fontsize=18)