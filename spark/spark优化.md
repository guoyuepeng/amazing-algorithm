- spark优化
https://tech.meituan.com/spark-tuning-basic.html
https://tech.meituan.com/spark-tuning-pro.html
  - 2-4 partitions for each CPU
  - 尽量避免使用shuffle类算子：shuffle过程中，各个节点上的相同key都会先写入本地磁盘，然后其他节点需要通过网络传输拉取各个节点上的磁盘文件中的相同key。而且相同key都拉取到同一个节点进行聚合操作时，还有可能会因为一个节点上处理的key过多，导致内存不够存放，进而溢写到磁盘文件中。因此在shuffle过程中，可能会发生大量的磁盘文件读写的IO操作，以及数据的网络传输操作。磁盘IO和网络数据传输也是shuffle性能较差的主要原因。尽量使用map等非shuffle算子
  - join减少shuffle:1. reaprtition(窄依赖，避免shuffle)： hash-partitioned, rdd.partitionBy(new HashPartitioner(num)).persist()
                          					            dataframe.repartition(num，colname to join) -- The resulting Dataset is hash partitioned.This is the same operation as   "DISTRIBUTE BY" in SQL (Hive QL). 
         2. Broadcast与map进行join操作
             // 传统的join操作会导致shuffle操作。
			// 因为两个RDD中，相同的key都需要通过网络拉取到一个节点上，由一个task进行join操作。
			val rdd3 = rdd1.join(rdd2)

			// Broadcast+map的join操作，不会导致shuffle操作。
			// 使用Broadcast将一个数据量较小的RDD作为广播变量。
			val rdd2Data = rdd2.collect()
			val rdd2DataBroadcast = sc.broadcast(rdd2Data)

			// 在rdd1.map算子中，可以从rdd2DataBroadcast中，获取rdd2的所有数据。
			// 然后进行遍历，如果发现rdd2中某条数据的key与rdd1的当前数据的key是相同的，那么就判定可以进行join。
			// 此时就可以根据自己需要的方式，将rdd1当前数据与rdd2中可以连接的数据，拼接在一起（String或Tuple）。
			val rdd3 = rdd1.map(rdd2DataBroadcast...)

			// 注意，以上操作，建议仅仅在rdd2的数据量比较少（比如几百M，或者一两G）的情况下使用。
			// 因为每个Executor的内存中，都会驻留一份rdd2的全量数据。
  - 多次使用的RDD进行持久化
  - 使用filter之后进行coalesce
  - 广播大变量
  - 适当增加 shuffle partition 个数，减少每个task的数据量

  1. shuffle partition 个数调优
  - 设置过小可能造成：Spill,OOM
  - 设置过大可能造成：更长的任务调度时间，更多IO请求，更多小文件输出
  - 同一个Shuffle Partition个数无法适应所有的Stage
  2. Spark Sql Join选择策略
  - Spark SQL在Planning阶段通过Join输入的大小来判断使用BroadcastHashJoin或者SortMergeJoin/HashShuffleJoin。一个复杂的Join可能使用中间结果作为输入。当Spark SQL在Planning阶段无法获取正确的Join输入大小时，导致无法选择最优的Join策略。
  3. Join中的数据倾斜
  - 数据倾斜意味着某些分区中的数据大小明显大于其他分区
  - 数据倾斜是Join性能变差的常见原因
  - 目前常见的手动解决倾斜的方法：
	- 增加Shuffle Partition个数
	- 增大BroadcastJoin阈值
	- 为倾斜的Key增加前缀特殊处理

https://blog.csdn.net/fl63zv9zou86950w/article/details/79049280


- 修改用户名，获得集群运行权限
export HADOOP_USER_NAME=""