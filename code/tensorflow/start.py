import numpy as np
import tensorflow as tf
import input_data


def test_code1():
    coefficients = np.array([[1], [-20], [25]])
    w = tf.Variable([0],dtype=tf.float32)
    x = tf.placeholder(tf.float32, [3,1])   # placeholder: 占位符
    cost = x[0][0]*w**2 + x[1][0]*w + x[2][0]

    train = tf.train.GradientDescentOptimizer(0.01).minimize(cost)
    init = tf.global_variables_initializer()
    session = tf.Session()
    session.run(init)
    print(session.run(w))
    for i in range(1000):
        session.run(train, feed_dict={x:coefficients})
        print(session.run(w))
    session.close()

def test_code2():
    # 使用 NumPy 生成假数据(phony data), 总共 100 个点.
    x_data = np.float32(np.random.rand(2, 100)) # 随机输入
    y_data = np.dot([0.100, 0.200], x_data) + 0.300

    # 构造一个线性模型
    b = tf.Variable(tf.zeros([1]))
    W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
    y = tf.matmul(W, x_data) + b

    # 最小化方差
    loss = tf.reduce_mean(tf.square(y - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    # 初始化变量
    init = tf.global_variables_initializer()

    # 启动图 (graph)
    sess = tf.Session()
    sess.run(init)

    # 拟合平面
    for step in range(0, 201):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(W), sess.run(b))

    # 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]
    sess.close()

def mnist():

    # step1：创建模型
    #　获取mnist数据集：返回DataSet实例
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    # 通过占位符生成训练集和标签x,y：任意数量的图像，每一张是784维
    x = tf.placeholder("float", [None, 784])
    y_ = tf.placeholder("float", [None, 10])
    # 定义参数w,b,并初始化为全零
    # Variable代表可修改的张量
    # 输出结果是10维
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    # 模型：单层softmax
    # tf.matmul：相乘
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    # 定义cost function：交叉熵
    cross_entropy = -tf.reduce_sum(y_*tf.log(y))
    # 优化算法：GD,learning_rate:0.01
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    # 初始化创建的变量
    init = tf.initialize_all_variables()


    # step2：运行模型
    # 在session中启动模型
    sess = tf.Session()
    sess.run(init)
    for i in range(1000):
        # 每batch随机抓取100个样本
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


    # step3：模型评估
    # tf.argmax:给出某个tensor对象在某一维上的其数据最大值所在的索引值
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

def weight_variable(shape):

    # 初始化参数全零不利于学习,因此用一个较小的正数来初始化权重
    # truncated_normal：截断正态分布 -- 在2倍标准差范围之内
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):

    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    # 卷积层
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    # 池化层
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

def mnist_optimizer():

    #　获取mnist数据集：返回DataSet实例
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    # 创建InteractiveSession类，它能让你在运行图的时候，插入一些计算图，在交互式环境中非常方便(如IPython)
    sess = tf.InteractiveSession()

    # 第一层卷积
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])

    # 第二层卷积




if __name__ == '__main__':

    mnist()
