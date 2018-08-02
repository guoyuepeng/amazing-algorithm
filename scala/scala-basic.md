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
- 