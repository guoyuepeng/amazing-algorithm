# scipy.cluster	向量量化
# scipy.constants	数学常量
# scipy.fftpack	快速傅里叶变换
# scipy.integrate	积分
# scipy.interpolate	插值
# scipy.io	数据输入输出
# scipy.linalg	线性代数
# scipy.ndimage	N维图像
# scipy.odr	正交距离回归
# scipy.optimize	优化算法
# scipy.signal	信号处理
# scipy.sparse	稀疏矩阵
# scipy.spatial	空间数据结构和算法
# scipy.special	特殊数学函数
# scipy.stats	统计函数

import numpy as np
from scipy import linalg  # 线性代数操作
arr = np.array([[1, 2],
                 [3, 4]])
linalg.det(arr)        # 计算行列式
arr = np.array([[3, 2],
                [6, 3]])
linalg.inv(arr)       # 矩阵的转置


from scipy import optimize  # 优化器
def f(x):
    return x**2 + 10*np.sin(x)
x = np.arange(-10, 10, 0.1)
optimize.fmin_bfgs(f, 0)

from scipy import stats   # 统计工具
a = np.random.normal(size=1000)
loc, std = stats.norm.fit(a)


# 在矩阵中，若数值为0的元素数目远远多于非0元素的数目，并且非0元素分布没有规律时，则称该矩阵为稀疏矩阵
from scipy.sparse import *
import matplotlib.pyplot as plt

# 双精度数据大小和内存之间的关系
x = np.linspace(0, 1e6, 10)
plt.plot(x, 8.0 * (x ** 2) / 1e6, lw=5)
plt.xlabel('size n')
plt.ylabel('memory [MB]')
plt.show()

M = np.array([1,0,0,0],[0,3,0,0],[0,1,1,0],[1,0,0,1])
# 把稠密矩阵变成稀疏矩阵
A = csr_matrix(M)
# 把稀疏矩阵变成稠密矩阵
A.todense()