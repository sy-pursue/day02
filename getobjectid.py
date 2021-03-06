from bson.objectid import ObjectId   #pymongo 2.2版本之后引入的方式
from pymongo import MongoClient

client = MongoClient("127.0.0.1",27017)
db = client.py08db
user = db.pyuser

ids = user.find({},{"_id":1})

values = []
for id_itme in ids:
    print(id_itme)
    values.append(id_itme['_id'])


id_value = values[0]
print(id_value)
res = user.find_one({'_id':id_value})
#res = user.find_one({'_id':ObjectId(id_value)})  #第二种方法
print(res)