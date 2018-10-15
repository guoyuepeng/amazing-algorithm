# 一.介绍
1. TensorFlow™ 是一个采用数据流图（data flow graphs），用于数值计算的开源软件库。节点（Nodes）在图中表示数学操作，图中的线（edges）则表示在节点间相互联系的多维数据数组，即张量（tensor）。
- 使用图(graph)来表示计算任务
    - 节点称之为op(operator),一个op获得0个或多个Tensor，执行计算，返回0个或多个Tensor
- 在被称之为会话(Session)的上下文(context)中执行图
    - 目的是节省资源开销？
    - 图必须在会话里被启动
    - 会话将图的op分发到CPU、GPU
    - 一般不需要显式指定CPU/GPU,TensorFLow会自动检测，优先使用GPU
    - 如果机器上有超过一个可用的 GPU, 除第一个外的其它 GPU 默认是不参与计算的. 为了让 TensorFlow 使用这些 GPU, 你必须将 op 明确指派给它们执行
- 使用tensor表示数据
    - 类型化的多维数组：np.ndarray
- 通过变量(Variable)维护状态
- 使用feed和fetch可以为任意的操作赋值或者从其中获取数据

- 通常分成两个阶段
    - 构建阶段：将op的执行步骤，描述成一个图
    - 执行阶段：在会话中执行图中的op

- tensorflow board
