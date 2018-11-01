#! /usr/bin/python3
# coding=utf-8

import pandas as pd
from use_behavior_data import usercf,useriif,itemcf,itemiuf,itemnorm,lfm
from util import movielen_reader
from eval import evaluate

if __name__ == '__main__':

    # load data : userid,movieid,rating
    # trainset:6040 user,3673 movieid
    # testset:6036 user,3488 movieid
    trainset, testset = movielen_reader.read_rating_data(train_rate=0.8)

    # 1.1 user-cf
    uf = usercf.UserCF()
    uf.train(trainset)
    evaluate(uf, trainset, testset)

    # 1.2 USER-IIF
    user_iif = useriif.UserCF()
    user_iif.train(trainset)
    evaluate(user_iif, trainset, testset)

    # 2.1 item-cf
    item_cf = itemcf.ItemCF()
    item_cf.train(trainset)
    evaluate(item_cf, trainset, testset)

    # 2.2 item-iuf
    item_iuf = itemiuf.ItemIUF()
    item_iuf.train(trainset)
    evaluate(item_iuf, trainset, testset)

    # 2.3 item-norm
    item_norm = itemnorm.ItemNorm()
    item_norm.train(trainset)
    evaluate(item_norm, trainset, testset)

    # 3.1

    print("execute sucessfully!")
