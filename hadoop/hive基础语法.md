##　其它
- 表查看： desc/desc formatted/desc extended tablename
- 表容量大小查看(单位为G)：
hadoop fs -du hdfs://ns/user/hive/warehouse/tmp_hotelbijobdb.db/pricerisk_inland_featureaa|awk '{ SUM += $1 } END { print SUM/(1024*1024*1024)}'
- 转换geohash经纬度：get_point_coordinates(a.geohash)

## 窗口函数
- lead(parmeter,offset,null) over(partition by )—当前行之后给定偏移量的行的访问，lag—当前行之前，与lead相对
- last_value(parameter) over(partition by …order by ...)—取最后一个值，first_value( )—取第一个值
- sum( ) over(partition by )
- row_number() over(partition by user_id order by created_at desc) rk——降序排列，rk为序号

## 时间函数
- from_unixtime() : 将时间戳转换为时间格式  ----  select from_unixtime(1326988805,'yyyyMMddHH') from test
- from_unixtime(unix_timestamp(),'yyyy-MM-dd')：获取当前ｕｎｉｘ时间戳函数
- 日期转时间戳： unix_timestamp　　－－－　 select unix_timestamp(’2011-12-07 13:01:03′) from dual
- year() month() day() hour() minute() second() weekofyear()
- datediff() date_add() date_sub() to_date()
- 把integer转化成datetime格式 ：from_unixtime(unix_timestamp(reportversion, 'yyyyMMddHH')

    set hive.mapred.mode=nonstrict;
    select *  from table
    where dt>date_add(from_unixtime(unix_timestamp()),-1)

## 数学函数

- 标准差：stddev
- 取某一位置（百分比）的数：percentile_approx(order_amt,0.6)


## 操作表
- ALTER TABLE TABLE_NAME1 RENAME TO TABLE_NAME2;  --重命名表
- ALTER TABLE TABLE_NAME1 ADD COLUMN (COLUMN_NAME DATA_TYPE);  --增加列
- ALTER TABLE TABLE_NAME1 DROP PARTITION (COLUMN_NAME1=’…’);  --删除表的分区
- SHOW TABLES ‘关键字 _.*’;    --正则匹配表名，类似于oracle中LIKE
- show functions：查函数
- ====把文本导入表中
use tmp_htlbidb;
drop table if exists tmp_ibuorder;
create table tmp_ibuorder
(
orderid bigint
)
row format delimited
fields terminated by ','
STORED AS TEXTFILE;
LOAD DATA LOCAL INPATH 'ibu.txt' INTO TABLE tmp_htlbidb.tmp_ibuorder;

- json解析：SELECT get_json_object(src_json.json, '$.owner') FROM src_json
            json_tuple
            more: http://www.lamborryan.com/hive-json/

## 行列转换
- 行转列：col3,col4,col5列转成了value列
- explode:一行拆成多行
- lateral view：用于UDTF中将行转成列
select col1, col2, value
from orig_table lateral view explode(array(col3,col4,col5)) orig_table_alias as value;
- 列转行
select col1,col2,concat_ws(',',collect_set(col3))
from orig_table_alias
group by col1,col2;


## 字符串
- 字符串操作：http://www.superwu.cn/2015/06/04/2690/
- regexp_replace(Content, '\'', '"')
- 字符串截取函数：left ('源字符串','要截取的最左边的字符数' )，right (同上 )
- substring (character,start,length)
- concat_ws(',', collect_set(building_name))
- CONCAT(字符A，字符B)与oracle用法相同；substr、ceil、floor、log、sqrt、round、to_data等常用函数与oracle相同

## 优化
当输入文件很大，而map数确很少时，每个map上job压力太大，可以增加map数量
set mapreduce.input.fileinputformat.split.maxsize=5000000;
set mapreduce.input.fileinputformat.split.minsize=5000000;

or  set mapred.map.tasks = 100
or
set hive.merge.mapfiles=false;
set hive.input.format=org.apache.hadoop.hive.ql.io.HiveInputFormat;

增加reducer个数
set mapred.reduce.tasks = 15;

获取表结构
select *
from INFORMATION_SCHEMA.COLUMNS
where TABLE_NAME='finf_stmt_is_indu'
