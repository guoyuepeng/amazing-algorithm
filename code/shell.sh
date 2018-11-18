#!/usr/bin/env bash

## awk : 文本处理语言

## 标准输入、标准输出和标准错误输出

# 标准输出(stdout)：终端的输出
# 标准错误(stderr)：程序出错时的反馈
# 标准输入(stdin)：程序指示输入的
# 输出重定向：将显示到屏幕上的反馈输出到文件

git push > log.txt

# 默认只重定向stdout，没重定向stderr

#- 1代表标准输出
#- 2代表标准错误
#- 2>&1 : stderr重定向到stdout

git push > log.txt 2>&1  # 标准输出、标准错误全都存到log.txt


## 如果报一些奇怪的错，考虑是EOL没有转换成unix格式

########## 文件管理 ################
# 服务器之间文件拷贝
scp -P 22 -r folder hotelbi@10.8.118.76:/home/hotelbi/swq/
scp -P 22 1.csv songwq@10.9.85.2:/home/songwq
rz -y # 上传

########## 包管理 ################
wget # 下载
apt-get install # 安装包
pip install modulename
pip install modulename --upgrade # 更新
conda ?

########## 文本编辑 ################
cat -A # 查找文件不可见字符
cat file1 file2 # 文件拼接

########## 系统管理 ################
linux版本查看：lsb_release -a
多少位 file /bin/ls
查看linux安装的软件：dpkg -l
查看某软件版本：python --version

内存 free-m
资源占用 top
硬盘空间：df -h
session资源占用：ps aux --sort=rss

# 查看物理CPU个数
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l

# 查看每个物理CPU中core的个数(即核数)
cat /proc/cpuinfo| grep "cpu cores"| uniq

# 查看逻辑CPU的个数
cat /proc/cpuinfo| grep "processor"| wc -l

# 查看CPU信息（型号）
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c

查看英伟达GPU  nvidia-smi

查看系统版本： cat /proc/version

查找文件： find -name [path...] [expression]
                         'filename*'---文件中带filename的

sed -n '5,10p' filename 这样你就可以只查看文件的第5行到第10行。

查看文件指定行内容  sed -n  'x,yp'  filename

VIM
-- 清空文件内容;gg--跳至首行，再dG

文件夹大小查看： du -h --max-depth=1
文件大小查看，排序： du -sh * | sort -rn
按照修改时间查看文件：ls -lt

统计某一路径下文件数量
ls -l |grep "^-"|wc -l

修改文件权限
sudo chmod o=rwx foldername  / u:user,g:group,o:others

sudo-i —得到超级权限
whereis+程序名—查找程序安装的路径
查看系统多少位 getconf LONG_BIT

unzip --解压zip文件
tar xvf-解压缩
tar -xjf  -解压缩 tar.bz2文件
gzip -d  --解压.gz文件
tar   zxvf  解压tgz文件

打包：tar czvf FileName.tar DirName
      zip -q -r FileName.zip DirName(如：.)

curl ‘url地址’—从网页下载文件
control+A—回到命令行首
control+R —找历史命令
ls -ltr—按创建顺序显示文件

telnet登陆： telnet -l xianbao.zeng 10.0.250.128

kill进程  kill -s 9 PID

日期循环
datebeg='2016-07-01'
dateend='2016-09-29'
beg_s=`date -d "$datebeg" +%s`
end_s=`date -d "$dateend" +%s`
while [ "$beg_s" -le "$end_s" ]
do
calc_dt=`date -d @$beg_s +"%Y-%m-%d"`
echo $calc_dt
x1="...
"
hive -e "$x1"
beg_s=$((beg_s+86400))
done

pip install --user

改账户密码：passwd
测试网络连接： ping www.baidu.com 80

自动发邮件：bash run.sh
#!/usr/bin/env bash
anaconda_pip=/usr/local/anaconda3/bin/pip
if [[ -f ${anaconda_pip} ]]; then
    export PATH=/usr/local/anaconda3/bin/:$PATH
    export PYTHONIOENCODING=utf8
fi
#python3.5 signal_monitor.py > logs
if [[ $? -eq 0 ]]; then
    content=`cat /home/weiqing.song/weekly_summary/datayes/advisor/html/weekly_summary.html`
    sendEmail -f weiqing.song@datayes.com -t weiqing.song@datayes.com -u weekly_summary -m "$content" -s mail.wmcloud.com -o message-charset=utf-8
    #sendEmail -f ziang.wei@datayes.com -t jinming.wan@datayes.com,li.li@datayes.com,guangpeng.chen@datayes.com,liang.zhao@datayes.com -u factor_monitor -m "$content" -a data/factor_report.csv -a data/signal_ideal_report.csv -a data/signal_slo_report.csv -s mail.wmcloud.com -o message-charset=utf-8
    echo "monitor sendEmail: done"
fi

crontab设置定时任务：crontab -e
0 12 * * 6 bash /home/weiqing.song/.profile; cd /home/weiqing.song/weekly_summary/ && nohup bash run.sh > nohup.out &
查看：crontab -l

shell调用python
variable1=$(python tradedate.py 2>&1)

环境变量：特定名字的对象
# 全局修改
利用vim打开/etc/profile文件，用export指令添加环境变量
# 只对当前特定用户起作用
修改个人用户主目录下的.bashrc文件