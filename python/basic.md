## 环境变量设置
1. 用于当前终端
```
export PATH=$PATH:<你的要加入的路径>
```
终端关闭后失效
2. 用于当前用户
用户主目录下有一个.bashrc的隐藏文件
```
export PATH=<你的要加入的路径>:$PATH
# 加入多个路径
export PATH=<你要加入的路径1>:<你要加入的路径2>: ...... :$PATH
# 生效
source ~/.bashrc
```
3. 用于所有用户
```
sudo gedit /etc/profile 
export PATH=<你要加入的路径>:$PATH
```

## python启动路径，package搜索路径
- python启动路径：PATH里面最后一个路径
- package搜索路径： PYTHONPATH
  - 命令窗口添加
    ```
    export PATH=$PATH:<你的要加入的路径>
    ```
  - python脚本中添加
    ```
    import sys
    sys.path.append(你的要加入的路径)
    ```
  - 跑python script前添加搜索路径
  ```
  PYTHONPATH=newpath python somescript.py somecommand
  ```
