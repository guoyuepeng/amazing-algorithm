# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import math
from user_based import GetRecommendation

def Recall(train,test,N):

    """
    Calculate recall of top N recommendation_in_action -- 有多少比例的用户有效行为记录包含在最终的推荐列表中

    Argument:
    train -- train data of dict (key:user,value:product)
    test -- test data of dict
    N -- top N

    Returns:
    recall
    """

    hit = 0
    all = 0
    for user in train.keys():
        tu = test(user)
        rank = GetRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit +=1
        all += len(tu)

    recall = hit/(all*1.0) 

    return recall

def Precision(train,test,N):

    """
    Calculate precision of top N recommendation_in_action -- 最终的推荐列表中有多少是用户发生有效行为的

    Argument:
    train -- train data of dict (key:user,value:product)
    test -- test data of dict
    N -- top N

    Returns:
    precision
    """

    hit = 0
    all = 0
    for user in train.keys():
        tu = test(user)
        rank = GetRecommendation(user,N)
        for item,pui in rank:
            if item in tu:
                hit +=1
        all += N

    precision = hit/(all*1.0) 

    return precision

def Coverage(train,test,N):

    """
    Calculate covarage of top N recommendation_in_action -- 最终的推荐列表包含多大比例的物品

    Argument:
    train -- train data of dict (key:user,value:product)
    test -- test data of dict
    N -- top N

    Returns:
    covarage
    """
    recommend_items = set()
    all_items = set()

    for user in train.keys():
        for item in train[user].keys():
            all_items.add(item)
        rank = GetRecommendation(user,N)
        for item,pui in rank:
            recommend_items.add(item)

    covarage = len(recommend_items) / (len(all_items)*1.0)

    return covarage


def Popularity(train,test,N):

    """
    Calculate popularity of top N recommendation_in_action -- 推荐列表中物品的平均流行度

    Argument:
    train -- train data of dict (key:user,value:product)
    test -- test data of dict
    N -- top N

    Returns:
    ret
    """
    item_popularity = dict()
    
    for user,items in train.items():
        for item in items.keys():
            if item not in item_popularity:
                item_popularity[item] = 0
            item_popularity[item] += 1
    ret = 0
    n = 0
    for user in train.keys():
        rank = GetRecommendation(user,N)
        for item,pui in rank:
            # 物品的流行度分布满足长尾分布，取对数后，流行度的平均值更加稳定
            ret += math.log(1+item_popularity[item])
            n += 1
    ret /= n*1.0

    return ret