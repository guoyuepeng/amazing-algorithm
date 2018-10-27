## 简介
- 多范式语言：
    - 函数式：每个函数都是一个值
    - 面向对象：每个值都是一个对象
- scala可以和java无缝操作：Scala类可以调用Java方法，创建Java对象，继承Java类和实现Java接口。这些都不需要额外的接口定义或者胶合代码。
- 访问修饰符
    - private:带有此标记的成员仅在包含了成员定义的类或对象内部可见
    - protected:只允许保护成员在定义了该成员的的类的子类中被访问
    - public:在任何地方都可以被访问
- Scala 不支持 break 或 continue 语句，但从 2.8 版本后提供了一种中断循环的方式
```
// 导入以下包
import scala.util.control._

// 创建 Breaks 对象
val loop = new Breaks;

// 在 breakable 中循环
loop.breakable{
    // 循环
    for(...){
       ....
       // 循环中断
       loop.break;
   }
}
```    
- 类中定义的函数即方法

## 函数
- 递归函数

```
object Test {
   def main(args: Array[String]) {
      for (i <- 1 to 10)
         println(i + " 的阶乘为: = " + factorial(i) )
   }
   
   def factorial(n: BigInt): BigInt = {  
      if (n <= 1)
         1  
      else    
      n * factorial(n - 1)
   }
}
```

- 高阶函数
高阶函数（Higher-Order Function）就是操作其他函数的函数。

```
object Test {
   def main(args: Array[String]) {

      println( apply( layout, 10) )

   }
   // 函数 f 和 值 v 作为参数，而函数 f 又调用了参数 v
   def apply(f: Int => String, v: Int) = f(v)

   def layout[A](x: A) = "[" + x.toString() + "]"
   
}
```
- 匿名函数
箭头左边是参数列表，右边是函数体
```var inc = (x:Int) => x+1```
以上实例的 inc 现在可作为一个函数，使用方式如下
```var x = inc(7)-1```
- 函数柯里化(Currying)
将原来接受两个参数的函数变成新的接受一个参数的函数的过程。新的函数返回一个以原有第二个参数为参数的函数。
首先我们定义一个函数:

```def add(x:Int,y:Int)=x+y```
那么我们应用的时候，应该是这样用：add(1,2)

现在我们把这个函数变一下形：

```def add(x:Int)(y:Int) = x + y```
那么我们应用的时候，应该是这样用：add(1)(2),最后结果都一样是3，这种方式（过程）就叫柯里化。


## 闭包
闭包是一个函数，返回值依赖于声明在函数外部的一个或多个变量。

闭包通常来讲可以简单的认为是可以访问一个函数里面局部变量的另外一个函数。
```
var factor = 3  
val multiplier = (i:Int) => i * factor  
```

## 字符串
- Java.lang.string 类
- String 对象是不可变的，如果你需要创建一个可以修改的字符串，可以使用 String Builder 类
- printf：打印格式化字符串


## 数组
- import Array._
- 声明
```var z:Array[String] = new Array[String](3)```
- 多维数组
```var myMatrix = ofDim[Int](3,3)```
- range() 方法来生成一个区间范围内的数组

## 集合(Collection)
- scala.collection.immutable  scala.collection.mutable 
- 可变集合：可以修改，添加，移除一个集合的元素
- 不可变集合：永远不会改变
- 类型
    - List(列表)
        - 所有元素类型都相同
        - 列表不可变
        - 列表定义
        ```
        // 字符串列表
        val site: List[String] = List("Runoob", "Google", "Baidu")

        // 整型列表
        val nums: List[Int] = List(1, 2, 3, 4)

        // 空列表
        val empty: List[Nothing] = List()

        // 二维列表
        val dim: List[List[Int]] =
        List(
            List(1, 0, 0),
            List(0, 1, 0),
            List(0, 0, 1)
        )

        ```
        - 也可以写成
        ```

        // 字符串列表
        val site = "Runoob" :: ("Google" :: ("Baidu" :: Nil))

        // 整型列表
        val nums = 1 :: (2 :: (3 :: (4 :: Nil)))

        // 空列表
        val empty = Nil

        // 二维列表
        val dim = (1 :: (0 :: (0 :: Nil))) ::
                (0 :: (1 :: (0 :: Nil))) ::
                (0 :: (0 :: (1 :: Nil))) :: Nil

        ```
        - 基本操作：head,tail,isEmpty
        - 连接列表：List.concat() 或者 ::

    - Set(集合)
        - 没有重复对象
        - 分为可变（scala.collection.mutable.Set）和不可变(默认，scala.collection.immutable.Set)

    - Map(映射)
        - key，value
        - 键是唯一的
        - 也叫哈希表(Hash tables)
        - 可变(scala.collection.mutable.Map)，不可变(默认)

    - 元组
        - 不可变
        - 可以包含不同类型的元素

    - Option
    
    - Iterator(迭代器)
        - 不是一个集合，是一种用于访问集合的方法
        - 基本操作：next、hasNext
        - it.next()返回迭代器的下一个元素，并且更新迭代器的状态
          it.hasNext()检测集合中是否还有元素

## 类和对象
- 类是抽象的，不占用内存；对象是具体的，占用内存
- 使用new关键字来创建类的对象
- 一个scala源文件可以有多个类
- 继承
    - 使用extends关键字来继承一个类
    - 重写一个非抽象方法必须使用override修饰符
    - 只有主构造函数才可以往基类的构造函数里面写参数
    - 在子类中重写超类的抽象方法时，不需要使用override关键字
    - 只允许继承一个父类
- 单例对象
    - 单例模式：一个类只有一个对象实例
    - 关键字 object   
    - 伴生对象(companion object):单例对象与某个类共享同一个名称，可以互相访问其私有成员

## Trait(特征)
- 相当于Java的接口
- 可以定义属性和方法的实现
- Trait可以继承多个，实现了多重继承
- 关键字trait

## 模式匹配
- 关键字 case
- match 表达式通过以代码编写的先后次序尝试每个模式来完成计算，只要发现有一个匹配的case，剩下的case不会继续匹配
- 样例类:case class

## 正则表达式
- 包：Regex
- pattern findFirstIn str

## 异常处理
- 可以通过抛出异常的方式终止代码的运行：throw
- 捕获异常：catch字句是按次序捕捉的。因此，在catch字句中，越具体的异常越要靠前，越普遍的异常越靠后
          借用了模式匹配的思想来做异常的匹配
- 最普遍的异常：Throwable
- finally：不管是正常处理还是有异常发生时都需要执行的步骤


## 提取器(Extractor)
- 提取器是从传递给它的对象中提取出构造该对象的参数。


## 文件IO
- java.io.File
- 新建文件，读取用户输入，读取文件内容。。。

## “_"的含义
- https://my.oschina.net/joymufeng/blog/863823
- 导入包时通配符
- 类成员默认值
- 访问tuple元素
