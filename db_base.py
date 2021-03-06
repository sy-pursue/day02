from mongodb_base import MC
from mongodb_operation import BaseHandle

class DBBase(object):  # 这个类是操作数据库
    def __init__(self, collection):
        self.mc = MC()  # 实例化类MC
        self.collection = self.mc.db[collection]

    def insert_one(self, data):
        res = BaseHandle.insert_one(self.collection, data)  # self.connection是表（集合）名，data是数据
        return res  # 返回一个id

    def insert_many(self, data_list):
        res = BaseHandle.insert_many(self.collection, data_list)
        return res

    def find_one(self, data, data_field={}):
        res = BaseHandle.find_one(self.collection, data, data_field)
        return res

    def find_many(self, data, data_field={}):
        # 如果有多个键值的话，此时 键值的关系就是 and 关系
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_all(self,data={},data_field={}):
        # select * from XXX;
        # res = self.find_many(data,data_field)  #调用私有方法
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_in(self, filed, item_list, data_field={}):
        data = dict()
        data[filed] = {"$in": item_list}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_or(self, data_list, data_field={}):
        data = dict()
        data["$or"] = data_list
        res = BaseHandle.find_many(self.collection,data,data_field)
        return res

    def find_like(self, filed, value, data_field={}):
        data = dict()
        data[filed] = {'$regex': '.*'+value+'.*'}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res