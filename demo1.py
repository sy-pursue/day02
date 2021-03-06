from pymongo import MongoClient as MC
'''
Python 操作 MongoDB的第三方包是 pymongo
用来对MongoDB数据库进行 数据的 管理一系列的操作

NoSQL 是支持横向扩展
横向扩展 也叫水平扩展 它是用更多的节点来支撑更大量的数据和请求
纵向扩展 也叫垂直扩展 它是扩展一个点的能力支撑更大的数据和请求

'''

'''
1、建立MongoDB 数据库连接
'''

client = MC('localhost',27017)  #第一种方法
#client = MC('mongodb://127.0.0.1:27017') 第二种方法

'''
2、连接指定数据库
'''
db = client.py06db
print(type(db.collection_names))
#获取当前指定数据库中的所有collection集合
print(db.collection_names())

'''
3、获取指定的collection集合
'''
grade_1_3 = db.grade_1_3
'''
对指定的表进行条件查询
'''
documents = grade_1_3.find()
print(documents)
for document in documents:
    print(document)



documents = grade_1_3.find({'age':{'$lt':22,'$gt':8}})
print(documents)
for document in documents:
    print(document)

documents = grade_1_3.find_one({'age':10})
print(documents)

#高级查询
age_sort = grade_1_3.find({'age':{'$type':1}},{'name':1,'age':1}).sort('name',1)
print(age_sort)
for item in age_sort:
    print(item)

'''
5、获取指定collection的个数
'''
print(grade_1_3.count())

'''
6、插入操作 insert_one()\insert_many()
Python3.X 之后 推荐的使用方法
'''
user_1 = {
    "name":"张三丰",
    "age":108,
    "hobby":[
        "武当",
        "太极"
    ]
}

grade_1_3.insert_one(user_1)
for document in grade_1_3.find():
    print(document)


user_2 = {
    "name":"张无忌",
    "age":50,
    "hobby":[
        "武当",
        "太极"
    ]
}


user_3 = {
    "name":"赵信",
    "age":30,
    "hobby":[
        "干掉王校长",
        "焰无尽"
    ]
}

grade_1_3.insert_many([user_2, user_3]) #不能重复插入一条数据，插入多条数据时插入格式应为列表类型
for document in grade_1_3.find():
    print(document)

'''
7、删除 指定集合中的数据
delete_one() / delete_many()
'''
grade_1_3.delete_one({"name": "张三丰"})

for item in grade_1_3.find({"name": "张三丰"}):
    print(item)

grade_1_3.delete_many({"name": "张三丰"})

for item in grade_1_3.find():
    print(item)