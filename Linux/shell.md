## awk

## 标准输入、标准输出和标准错误输出

- 标准输出(stdout)：终端的输出
- 标准错误(stderr)：程序出错时的反馈
- 标准输入(stdin)：程序指示输入的

- 输出重定向：将显示到屏幕上的反馈输出到文件
```
git push > log.txt
```
默认只重定向stdout，没重定向stderr

- 1代表标准输出
- 2代表标准错误
- 2>&1 : stderr重定向到stdout
```
git push > log.txt 2>&1  # 标准输出、标准错误全都存到log.txt
```