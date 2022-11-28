# 处理数据库中多表关联同步es处理,包括1对1,1对多的对应关系
* 具体映射设置参照[mapping.yml](https://github.com/Velsson/cannal_mysql_elasticsearch/blob/master/src/main/resources/mapping.yml)文件  

* 在处理全量同步时参考[实体](https://github.com/Velsson/cannal_mysql_elasticsearch/blob/master/src/main/java/com/veelur/sync/elasticsearch/model/request/SyncByIndexRequest.java)  
类似http://localhost:8828/dada/sync/byIndex?index=student&type=student&orderSign=id&start=0&end=100&limit=500&orderType=long   
  同步索引index： user           ---需要同步的索引名   
  索引类型type： user            ---需要同步的索引类型   
  排序字段orderSign： id         ---索引对应主表的标识字段,如主键或创建时间等    
  排序字段类型orderType: long     ---标识字段类型,可选值：string,long,double,date    
  开始start： 0                 ---标识字段的开始值(时间格式满足:yyyy-MM-dd HH:mm:ss)    
  结束enbd： 100                ---标识字段的结束值(时间格式满足:yyyy-MM-dd HH:mm:ss)   
  每次处理条数limit: 100         ---处理线程每次处理的数据条数,默认为200条
 

* wiki在编写中...

* 测试情况： 4线程并发插入3张表,每张表2000数据量,三张表对应与同一个索引  
最少耗时：148ms     
最大耗时：1980ms  
正常情况：100-300ms  
处理时间(从获取到binlog到完成同步elastic)：4-70ms   
* 若处理时间存在差异，可以查看是否有网络传输问题,除了elastic的操作，其他皆为纯内存操作

* 目前v2.0.0着力于整合canal,取消繁杂的canal服务搭建及不必要的网络传输
