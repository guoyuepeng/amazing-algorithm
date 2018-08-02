## 

## Dataset,DataFrame,RDD 比较
相同：
	- 惰性机制
	- 根据内存情况自动缓存运算？
	- partition概念，如mappartition对每一个分区进行操作，数据量小，而且可以将运算结果拿出来，map中对外面变量的操作是无效的
	- 有共同的方法，如filter、排序等
不同：
    - RDD:不支持spark sql，支持spark mllib
    - DataFrame、Dataset：支持spark ml、spark sql
DataFrame VS Dataset
	DataFrame：Dataset[Row]，每一行的类型是Row
	Dataset访问列中的某个字段方便
转化
	DataFrame/Dataset 转RDD df.rdd
	RDD转DataFrame：import spark.implicits._
					val testDF = rdd.map {line=>
					      (line._1,line._2)
					    }.toDF("col1","col2")
	RDD转DataSet：import spark.implicits._
					case class Coltest(col1:String,col2:Int)extends Serializable //定义字段名和类型
					val testDS = rdd.map {line=>
					      Coltest(line._1,line._2)
					    }.toDS
	Dataset转DataFrame：   import spark.implicits._
							val testDF = testDS.toDF	
	DataFrame转Dataset：	case class Coltest(col1:String,col2:Int)extends Serializable //定义字段名和类型
						val testDS = testDF.as[Coltest]					   			    

printing elements of RDD：rddforeach(println)---print to the executor's stdout,not the driver's stdout;
                          rdd.collect().foreach(println)--print to the driver's stdout

- 函数传递
1. 匿名函数：当函数代码比较短
2. 单例对象中的静态方法

- 闭包
代码+用到的局部变量

- 共享变量
广播变量
累加器：闭包（类似foreach）修改全局变量的操作结果不能保证，要使用累积器
       https://blog.csdn.net/u013468917/article/details/70617085
