'''
MongoDB中的普通查询也是通过一条条数据进行过滤，直到匹配条件为止
为了能快速遍历，MongoDB 引入index索引
如果没有索引，MongoDB 在读取数据时必须扫描集合中每一个文件
扫描效率低，特别是大量数据时，查询可以花费几十毫秒甚至几分钟，对网站的性能是非常致命的
索引是特殊的数据结构，设置索引之后，索引被存储在一个易于遍历读取的数据集合中，
索引是对数据库中一列或者多列的值进行排序的一种结构
在 终端中 MongoDB 创建索引的方法为：
db.collection,createIndex(keys,options)
keys 是要被创建为索引的字段，options 为1则表示升序创建索引 -1则表示降序创建索引

'''
from pymongo import MongoClient

client = MongoClient('127.0.0.1',27017)
db = client.py06db
student = db.students

student.create_index([('name',1)])

print(student.find().explain())
print(student.find().explain()['executionStats']['executionTimeMillis'])

print(student.find({'name':'test50000'}).explain()['executionStats']['executionTimeMillis'])