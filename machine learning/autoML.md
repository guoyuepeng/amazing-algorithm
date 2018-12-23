- 神经架构搜索(NAS)
    - 从一组神经网络可能会用到的模块开始，搜索出最好的神经网络架构
    - 采用一个RNN作为控制器
    - Learning Transferable Architectures for Scalable Image Recognition
    - 非常耗时
- 高效神经架构搜索(ENAS)
    - Efficient Neural Architecture Search via Parameter Sharing
- 局部自动学习解决方案
    - 特征工程
        - 自动构造特征
            - Featuretools : https://github.com/Featuretools/featuretools
        - 降维
            - Boruta-py : https://github.com/scikit-learn-contrib/boruta_py
        - 离散特征编码
            - Categorical-encoding ： https://github.com/scikit-learn-contrib/categorical-encoding
        - 时间序列数据的特征生成
            - Tsfresh ： https://github.com/blue-yonder/tsfresh
    - 超参数优化
        - Skopt：https://scikit-optimize.github.io/
        - Hyperopt：https://github.com/hyperopt/hyperopt-sklearn
        - Ray.tune ：　https://github.com/ray-project/ray/tree/master/python/ray/tune
    －　全流程解决方案
        －　auto-sklearn　：　https://github.com/automl/auto-sklearn
        －　H2O ： https://github.com/h2oai/h2o-3
        -  TPOT ： https://github.com/EpistasisLab/tpot
- AutoML
    - 只需要提供数据，就能自动创建出由复杂神经网络驱动的决策功能
    - 开源框架
        - autokeras：https://github.com/jhfjhfj1/autokeras
        - enas：https://github.com/melodyguan/enas
        - enas-pytorch：https://github.com/carpedm20/ENAS-pytorch
    - 主要问题
        - 特征工程
        - 模型选择
        - 算法选择：SGD，L-BFGS，GD


- 参考资料
《自动机器学习工具全景图：精选22种框架，解放炼丹师》
《第四范式涂威威：AutoML技术现状与未来展望》
