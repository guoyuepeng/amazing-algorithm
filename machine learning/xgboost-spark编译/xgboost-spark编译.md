比如需要把xgboost跑到集群上，最好选一台集群中的结点（或者配置相同的机器），做下面操作，生成jar包

已知依赖：g++(4.8以上)

一、编译xgboost-C++模块

git clone --recursive https://github.com/dmlc/xgboost
git submodule init
git submodule update

或者直接用附件中的xgboost.tar.gz [这个版本是0.7，注意不是最新的]，并上传到某一台结点上
tar xvf xgboost.tar.gz (xgboost.tar.gz)
cd xgboost
make -j4

二、编译xgboost4j/spark模块，注意spark版本与集群版本一致

cd jvm-packages

bash create_jni.sh

mvn -Dspark.version=2.1.0 package

我们需要的jar包在，xgboost4j-spark/target/xgboost4j-spark-0.7-jar-with-dependencies.jar

如果报错的话，可以修改pom.xml，在dependencies中添加，pom.xml 


三、测试jar包跨平台运行 

- 要在集群的每个节点上都测试通过才可以

以下几个文件放到同一个路径
- agaricus.txt.test
- agaricus.txt.train
- PredictFirstNtree.java
- 上步得到的jar包

javac -cp ./xgboost4j-spark-0.7-jar-with-dependencies_linux_cluster.jar PredictFirstNtree.java
java -cp ./xgboost4j-spark-0.7-jar-with-dependencies_linux_cluster.jar: PredictFirstNtree

正确输出结果，则表明xgboost编译成功


四. 最好通过集群的其中一个节点提交任务