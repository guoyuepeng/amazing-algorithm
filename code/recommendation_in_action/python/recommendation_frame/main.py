#! /usr/bin/python3
# coding=utf-8

from use_behavior_data import usercf
from imp import reload
from util import movielen_reader


if __name__ == '__main__':

    # load data : userid,movieid,rating
    # trainset:6040 user,3673 movieid
    # testset:6036 user,3488 movieid
    trainset, testset = movielen_reader.read_rating_data(train_rate=0.8)

    # 1.1 user-cf
    uf = usercf.UserCF()
    uf.train(trainset)

    # evaluation



    # 1.2 USER-IIF

    # 2.1 item-cf

    print("execute sucessfully!")
