#! /usr/bin/python3
# coding=utf-8
import pandas as pd
from util import metric
from util import movielen_reader

def train_popularity(train):
    """计算训练集商品的流行度：商品的数量"""
    train_popularity = dict()
    for user, item, _ in train:
        train_popularity.setdefault(item, 0)
        train_popularity[item] += 1
    return train_popularity


def topN(model,trainset,testset, N, K):
    """评价模型
        Args:
            model : 推荐模型
            trainset/testset : 训练集/测试集
            N:　　　　推荐的商品个数
            K:　　　　搜索邻近的用户个数
        Return:
            精确率,召回率,覆盖率,流行度
    """

    test = dict()
    for user, item, _ in testset:
        test.setdefault(user, list())
        test[user].append(item)

    recommens = model.recommend_users(test.keys(), N=N, K=K)
    all_items = movielen_reader.all_items()
    item_popularity = train_popularity(trainset)

    recall = metric.recall(recommends=recommens, tests=test)
    precision = metric.precision(recommends=recommens, tests=test)
    coverage = metric.coverage(recommends=recommens, all_items=all_items)
    popularity = metric.popularity(item_popular=item_popularity, recommends=recommens)

    return precision, recall, coverage, popularity

def evaluate(uf,trainset,testset):

    N = 30  # 表示推荐的商品个数
    K_list = [5, 10, 20, 40, 80, 160]  # 表示临近用户的list
    evals = list()

    for k in K_list:
        single_eval = topN(uf,trainset,testset,N=N, K=k)
        evals.append(single_eval)

    results = pd.DataFrame(
        data=evals,
        index=K_list,
        columns=["Precision", "Recall", "Coverage", "Popularity"]
    )

    print(results.head(10))