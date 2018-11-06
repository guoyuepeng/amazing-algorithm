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

    trainset = trainset[:int(len(trainset) / 10)]
    testset = testset[:int(len(testset) / 10)]

    # 1.1 user-cf
    uf = usercf.UserCF()
    uf.train(trainset)
    evaluate(uf, trainset, testset)
    print("train user-cf model done!")

    # 1.2 USER-IIF
    user_iif = useriif.UserIIF()
    user_iif.train(trainset)
    evaluate(user_iif, trainset, testset)
    print("train user-iiff model done!")

    # 2.1 item-cf
    item_cf = itemcf.ItemCF()
    item_cf.train(trainset)
    evaluate(item_cf, trainset, testset)
    print("train item-cf model done!")

    # 2.2 item-iuf
    item_iuf = itemiuf.ItemIUF()
    item_iuf.train(trainset)
    evaluate(item_iuf, trainset, testset)
    print("train item-iuf model done!")

    # 2.3 item-norm
    item_norm = itemnorm.ItemNorm()
    item_norm.train(trainset)
    evaluate(item_norm, trainset, testset)
    print("train item-norm model done!")

    # 3.1

    print("execute sucessfully!")
