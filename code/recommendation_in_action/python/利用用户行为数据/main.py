# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import os
print(os.getcwd())




if __name__ == '__main__':

    ratings = pd.read_table("../../../dataset/ml-1m/ratings.dat", sep="::", header=None,
                            names=["userid", "movieid", "rating", "timestamp"])
    users = pd.read_table("../../../dataset/ml-1m/users.dat", sep="::", header=None,
                          names=["userid", "gender", "age", "occupation"])
    movies = pd.read_table("../../../dataset/ml-1m/movies.dat", sep="::", header=None,
                           names=["title", "genres"])

    # 目标：预测用户是否会对电影评分
    # 构建隐式反馈的数据集
    dataset = ratings[['userid', 'movieid']]

    # user-based

    # item-based

    print("execute sucessfully!")
