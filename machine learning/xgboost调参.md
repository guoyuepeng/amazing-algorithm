- XGBOOST
6.1  经过优化的分布式、基于CART的迭代boosting算法
 6.2  Boosting：
-  	将弱学习器提升为强学习器。先从初始训练集训练出一个基学习器，再根据基学习器的表现对训练样本分布进行调整，使得先前在基学习器中学错的训练样本在后续得到更多的关注，然后基于调整后的样本分布来训练下一个基学习器。如此重复进行，直至基学习器数目达到事先指定的值T。最终将这T个基学习器进行加权结合。
-  	个体学习器间存在强依赖关系，必须串行生成的序列化方法。
-  	AdaBoost、GBDT、XGBOOST
6.3 Bagging
-  	即Bootstrap AGGregatING. 通过有放回的采样出T个含m个训练样本的采样集，然后基于每个采样集训练出一个基学习器，再将这些基学习器进行结合。在对预测输出进行结合时，通常对分类任务采用简单投票法，对回归任务采用简单平均法。
-  	个体学习器间不存在强依赖关系，可同时生成的并行化方法。
-  	随机森林
6.4 XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. It implements machine learning algorithms under the Gradient Boosting framework. XGBoost provides a parallel tree boosting (also known as GBDT, GBM) that solve many data science problems in a fast and accurate way. The same code runs on major distributed environment (Hadoop, SGE, MPI) and can solve problems beyond billions of examples.
6.5 优点
-  	效果好：xgboost则对代价函数进行了二阶泰勒展开，同时用到了一阶和二阶导数；
-  	并行计算，速度快：gboost的并行是在特征粒度上的，决策树的学习最耗时的一个步骤就是对特征的值进行排序（因为要确定最佳分割点），xgboost在训练之前，预先对数据进行了排序，然后保存为block结构，后面的迭代中重复地使用这个结构，大大减小计算量。这个block结构也使得并行成为了可能，在进行节点的分裂时，需要计算每个特征的增益，最终选增益最大的那个特征去做分裂，那么各个特征的增益计算就可以开多线程进行；
-  	抗过拟合能力强：在代价函数里面加上了正则项，用于控制模型的复杂度；
-  	支持列抽样；
-  	学习速率，削弱每棵树的影响，让后面有更大的学习空间；
-  	自带特征筛选功能；
-      可并行的近似直方图算法。树节点在进行分裂时，我们需要计算每个特征的每个分割点对应的增益，即用贪心法枚举所有可能的分割点。当数据无法一次载入内存或者在分布式情况下，贪心算法效率就会变得很低，所以xgboost还提出了一种可并行的近似直方图算法，用于高效地生成候选的分割点。
6.6 作者理解的boosting是Additive training，每一次保留原来的模型不变，加入一个新的函数f到我们的模型。如何选取：选取一个使得我们的目标函数尽量最大地降低的f。

6.7 怎么解释模型（如XGBOOST）
n  变量重要性
Gain is the improvement in accuracy brought by a feature to the branches it is on. The idea is that before adding a new split on a feature X to the branch there was some wrongly classified elements, after adding the split on this feature, there are two new branches, and each of these branch is more accurate (one branch saying if your observation is on this branch then it should be classified as 1, and the other branch saying the exact opposite).
 
Cover measures the relative quantity of observations concerned by a feature.
 
Frequency is a simpler way to measure the Gain. It just counts the number of times a feature is used in all generated trees. You should not use it (unless you know why you want to use it).




具体XGBOOST的原理可以参见之前的文章《比XGBOOST更快--LightGBM介绍》
今天说下如何调参。
bias-variance trade-off
xgboost一共有几十个参数：
http://xgboost.readthedocs.io/en/latest/parameter.html
中文版解释：
http://blog.csdn.net/zc02051126/article/details/46711047


文艺青年的调参一般这样的：
1. 设定参数{parm}，评判指标{metrics}；
2. 根据{metrics}在验证集上的大小，确定树的棵树n_estimators；
3. 采用参数{parm}、n_estimators，训练模型，并应用到测试集
一个字：糙！（kuai）
数据挖掘师的调参一般这样的：
1. 设定基础参数{parm0}，基础评判指标{metrics0}；
2. 在训练集上做cross-validation，做训练集/交叉验证集上偏差/方差与树棵树的关系图；
3. 判断模型是过拟合 or 欠拟合，更新相应参数{parm1}；
4. 重复2、3步，确定树的棵树n_estimators；
5. 采用参数{parm1}、n_estimators，训练模型，并应用到测试集；

举个栗子：
数据集大小：70000*100，随机准确率 0.17%
在设置了基础参数，设定了树的范围后，可以看到模型在训练集和交叉验证集上的效果是这样子滴：

![valid.png](valid.png)

阴影部分，表示的是模型的方差
从上图，可以得出以下几个结论：
- 验证集上偏差最小&方差最小：n_estimators=66
- 训练集和验证集误差较大：过拟合-----模型过于复杂
- 方差较大----模型过于复杂
这符合下面这个图

![bias-variance.png](bias-variance.png)

以上特征，都表明我们需要降低模型复杂程度，有哪些参数可以调整呢：
- 直接降低模型复杂度
max_depth、min_child_weight、gamma
- 随机化
subsample、colsample_bytree
- 正则化
lambda、alpha
通过，grid-search，再调整了以上的参数后，如下图。最佳trade-off点的variance从0.361降低到0.316，auc_mean从0.8312降低到0.8308。



P-R的提升还是比较明显的：




还有，先粗调，再微调
-- 降低learning_rate，当然同时，提高n_estimators



2. 非平衡数据集怎么办
-- 想办法弄到更多的数据
-- 想办法把数据弄平衡
-- 利用smote等算法来过采样/欠采样
-- 设置weight（初始化DMatrix时）
-- 使用更好的metrics：auc、f1
-- min_child_weight 设的小一点
-- scale_pos_weight = 0值的样本数量/1值的样本数量
-- max_delta_step
-- 自定义评价函数
xgb.train(params, dtrain, num_rounds, watchlist, feval=misclassified, maximize=False)
def misclassified(pred_probs, dtrain):
    labels = dtrain.get_label() # obtain true labels
    preds = pred_probs > 0.5 # obtain predicted values
    return 'misclassified', np.sum(labels != preds)

