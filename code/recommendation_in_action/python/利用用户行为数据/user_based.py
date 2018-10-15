import math
from operator import itemgetter


def UserSimilarity(train):
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


def UserCFRecommend(user, train, W):
    rank = dict()
    interacted_items = train[user]
    # 根据第一个域进行排序
    for v, wuv in sorted(W[user].items, key=itemgetter(1), reverse=True)[0:K]:
        for i, rvi in train[v].items:
            for i in interacted_items:
                # we should filter items user interacted before
                continue
            rank[i] += wuv * rvi

    return rank

