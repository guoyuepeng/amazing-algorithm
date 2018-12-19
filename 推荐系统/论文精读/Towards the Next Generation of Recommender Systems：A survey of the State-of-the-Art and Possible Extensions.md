《Towards the Next Generation of Recommender Systems：A survey of the State-of-the-Art and Possible Extensions》

推荐问题：预测用户对商品的偏好

符号：s--item，c--user

1. Content-based
    - 利用物品的文本信息
    - tf-idf得到文本向量:Content(s)
    - 根据用户历史行为，得到用户的ContentBasedProfile(c)
        - average approach：Rocchio algorithm
        - Bayesian classifier：Winnow algorithm
        - 计算score(Content(s),ContentBasedProfile(c)) 
            - heuristic:余弦相似度
            - statistical learning /machine learning 
    - 局限
        - 被物品特征限制
        - 如果两篇文章关键词相同，很难区分好坏
        - 推荐的物品跟用户历史偏好的物品相似度高  -- 可以引入一些随机性
        - 新用户无法推荐

2. Collaborative recommendations
    - memory-based(heuristic-based)
    - model-based
3. Hybrid approaches
