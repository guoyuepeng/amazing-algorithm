#-*- coding: utf-8 -*-

import os

'''
write code self
'''

class UserBasedCF(object):

    def __init__(self):

        self.trainset = {}
        self.testset = {}


if __name__ == '__main__':

    ratingfile = "../../../dataset/ml-1m/ratings.dat"
    usercf = UserBasedCF()
    usercf.generate_dataset(ratingfile)
    usercf.calc_user_sim()
    usercf.evaluate()