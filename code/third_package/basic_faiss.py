import numpy as np

# https://blog.csdn.net/kanbuqinghuanyizhang/article/details/80774609

d = 64                           # dimension
nb = 100000                      # database size
nq = 10000                       # nb of queries
np.random.seed(1234)             # make reproducible
xb = np.random.random((nb, d)).astype('float32') # 训练数据
xb[:, 0] += np.arange(nb) / 1000.
xq = np.random.random((nq, d)).astype('float32') # 查询数据
xq[:, 0] += np.arange(nq) / 1000.


# 创建索引,faiss创建索引对向量预处理，提高查询效率。
index = basic_faiss.IndexFlatL2(d)   # build the index
print(index.is_trained)

index.add(xb)                  # add vectors to the index
print(index.ntotal)

# 传入搜索向量查找相似向量
k = 4                          # we want to see 4 nearest neighbors
D, I = index.search(xq, k)     # actual search
print(I[:5])                   # neighbors of the 5 first queries
print(D[-5:])                  # neighbors of the 5 last queries

