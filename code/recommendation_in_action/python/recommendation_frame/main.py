#! /usr/bin/python3
# coding=utf-8

from use_behavior_data import usercf
from imp import reload
from util import movielen_reader


if __name__ == '__main__':

    # load data
    trainset, testset = movielen_reader.read_rating_data(train_rate=0.8)

    # user-cf
    uf = usercf.UserCF()
    uf.train(trainset)

    # evaluation

    # item-cf

    print("execute sucessfully!")
