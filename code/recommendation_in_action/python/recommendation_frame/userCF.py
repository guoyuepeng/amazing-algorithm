import math
from operator import itemgetter


def UserSimilarity(train):
    '''
    :param train: 训练集,用户行为数据,dict(user:items:rui(兴趣))
    :return: W,dict格式,W[u][v]是用户u和v的余弦相似度
    '''
    # build inverse table for item:users
    item_users = dict()
    for u, items in train.items():
        for i in items.keys():
            if i not in item_users:
                item_users[i] = set()
            item_users[i].add(u)

    # calculae co-rated items between users
    C = dict()
    N = dict()
    for i, users in item_users.items():
        for u in users:
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                C[u][v] += 1

    # calculate finial similarity matrix W
    W = dict()
    for u, related_users in C.items():
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u] * N[v])

    return W


def UserCFRecommend(user, train, W, K):
    '''
    :param user: 目标用户
    :param train: 训练集
    :param W: 相似度dict
    :param K: 推荐给目标用户最相似的K个用户喜欢的物品
    :return: dict(key--推荐物品,value--打分)
    '''
    rank = dict()
    # 目标用户已有行为产品
    interacted_items = train[user]
    # 取最相似的K个用户
    for v, wuv in sorted(W[user].items, key=itemgetter(1), reverse=True)[0:K]:
        for i, rvi in train[v].items:
            for i in interacted_items:
                # we should filter items user interacted before
                continue
            rank[i] += wuv * rvi

    return rank

