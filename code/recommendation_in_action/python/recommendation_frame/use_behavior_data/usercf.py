#! /usr/bin/python3
# coding=utf-8
from collections import defaultdict
import math
from operator import itemgetter
import sys
from util.utils import load_file,save_file

class UserCF(object):
    """
    用户协同过滤
    使用隐式反馈,所有用户对商品的打分都是1
    """

    def __init__(self):
        pass
    
    def train(self, origin_data, sim_matrix_path="store/user_sim.pkl"):
        """训练模型
            @param origin_data: 原始数据 
            @param sim_matrix_path:  协同矩阵保存的路径
        """
        self.origin_data = origin_data
        # 初始化训练集
        self._init_train(origin_data)
        print("开始训练模型",file = sys.stderr)  # print to stderr ?
        try:
            print("开始载入用户协同矩阵....",file = sys.stderr)
            self.user_sim_matrix = load_file(sim_matrix_path)
            print("载入协同过滤矩阵完成",file = sys.stderr)
        except:
            print("载入用户协同过滤矩阵失败，重新计算协同过滤矩阵",file = sys.stderr)
            # 计算用户协同矩阵
            self.user_sim_matrix = self.user_similarity()
            print("开始保存协同过滤矩阵",file = sys.stderr)
            save_file(sim_matrix_path, self.user_sim_matrix)
            print("保存协同过滤矩阵完成",file = sys.stderr)

    def _init_train(self,origin_data):
        """
        初始化训练集数据:dict--user,items
        """
        self.train = dict()
        for user,item,_ in origin_data:
            self.train.setdefault(user,set())  # insert userid as key if not exists
            self.train[user].add(item)   # value is set format:items are unique

    def user_similarity(self):
        """建立用户的协同过滤矩阵"""
        #建立用户倒排表:key--item,value--users
        item_user = dict()
        for user,items in self.train.items():
            for item in items:
                item_user.setdefault(item,set())
                item_user[item].add(user)
                
        #建立用户-用户相似度矩阵
        user_sim_matrix = dict()
        # defaultdict类接受一个类型作为参数，当所访问的键不存在的时候，可以实例化一个值作为默认值
        N = defaultdict(int)    #记录用户购买商品数
        for item,users in item_user.items():
            for u in users:
                N[u] += 1
                for v in users:
                    if u == v:
                        continue
                    user_sim_matrix.setdefault(u,defaultdict(int))
                    user_sim_matrix[u][v] += 1
        
        #计算用户-用户余弦相似度
        for u,related_users in user_sim_matrix.items():
            for v,con_items_count in related_users.items():
                user_sim_matrix[u][v] = con_items_count / math.sqrt(N[u] * N[v])
        
        return user_sim_matrix 
    
    def recommend(self,user,N,K):
        """推荐
            @param user:   用户
            @param N:    推荐的商品个数
            @param K:    查找最相似的用户个数
            @return: 商品字典 {商品 : 相似性打分情况}
        """
        related_items = self.train.get(user,set) # 返回指定key的value
        recommmens = dict()
        for v,sim in sorted(self.user_sim_matrix.get(user,dict).items(),
                            key = itemgetter(1),reverse = True)[:K]:
            for item in self.train[v]:
                if item in related_items:
                    continue
                recommmens.setdefault(item,0.)
                recommmens[item] += sim 
        
        return dict(sorted(recommmens.items(),key = itemgetter(1),reverse = True)[ : N])
    
    def recommend_users(self,users,N,K):
        """为用户推荐商品
            @param users:    用户list
            @param N:    推荐的商品个数
            @param K:    查找最相似的用户个数
            @return: 推荐字典 {用户 : 推荐的商品的list}
        """
        recommends = dict()
        for user in users:
            user_recommends= list(self.recommend(user, N, K).keys())
            recommends[user] = user_recommends
            
        return recommends 
