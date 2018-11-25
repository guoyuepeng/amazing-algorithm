# https://github.com/marcotcr/lime
# lime这个解释器适用于任何我们想要用的任何分类器，只要这个分类器实现了predict_proba。
from __future__ import print_function
import lime
import sklearn
import numpy as np
import sklearn
import sklearn.ensemble
import sklearn.metrics
from sklearn.datasets import fetch_20newsgroups

categories = ['alt.atheism', 'soc.religion.christian']
newsgroups_train = fetch_20newsgroups(subset='train', categories=categories)
newsgroups_test = fetch_20newsgroups(subset='test', categories=categories)
class_names = ['atheism', 'christian']  # 两种标签，一种基督教，一种无神论

vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(lowercase=False)   ## 使用TF-IDF对文本进行编码
train_vectors = vectorizer.fit_transform(newsgroups_train.data)
test_vectors = vectorizer.transform(newsgroups_test.data)

# 使用RF模型
rf = sklearn.ensemble.RandomForestClassifier(n_estimators=500)
rf.fit(train_vectors, newsgroups_train.target)
# RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#             max_depth=None, max_features='auto', max_leaf_nodes=None,
#             min_samples_leaf=1, min_samples_split=2,
#             min_weight_fraction_leaf=0.0, n_estimators=500, n_jobs=1,
#             oob_score=False, random_state=None, verbose=0,
#             warm_start=False)

# 预测
pred = rf.predict(test_vectors)
sklearn.metrics.f1_score(newsgroups_test.target, pred, average='binary')

# 预测结果：0.92093023255813955

from lime import lime_text
from sklearn.pipeline import make_pipeline
c = make_pipeline(vectorizer, rf)
print(c.predict_proba([newsgroups_test.data[0]]))
# [[ 0.274  0.726]]

from lime.lime_text import LimeTextExplainer
explainer = LimeTextExplainer(class_names=class_names)

# 我们对任意一篇文章挑选出前6个重要的特征
idx = 83
exp = explainer.explain_instance(newsgroups_test.data[idx], c.predict_proba, num_features=6)
print('Document id: %d' % idx)
print('Probability(christian) =', c.predict_proba([newsgroups_test.data[idx]])[0,1])
print('True class: %s' % class_names[newsgroups_test.target[idx]])
# Document id: 83
# Probability(christian) = 0.414
# True class: atheism

print(exp.as_list())
# [(u'Posting', -0.15748303818990594),
# (u'Host', -0.13220892468795911),
# (u'NNTP', -0.097422972255878093),
# (u'edu', -0.051080418945152584),
# (u'have', -0.010616558305370854),
# (u'There', -0.0099743822272458232)]

print('Original prediction:', rf.predict_proba(test_vectors[idx])[0,1])
tmp = test_vectors[idx].copy()
tmp[0,vectorizer.vocabulary_['Posting']] = 0
tmp[0,vectorizer.vocabulary_['Host']] = 0
print('Prediction removing some features:', rf.predict_proba(tmp)[0,1])
print('Difference:', rf.predict_proba(tmp)[0,1] - rf.predict_proba(test_vectors[idx])[0,1])
# Original prediction: 0.414
# Prediction removing some features: 0.684
# Difference: 0.27

