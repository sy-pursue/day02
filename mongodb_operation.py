class BaseHandle(object):  # 为了方便修改语句（mongodb升级时，方法优化时）
    @staticmethod
    def insert_one(collection, data):  # 插入数据,collection是表（集合）名，data是数据
        res = collection.insert_one(data)
        return res.inserted_id

    @staticmethod
    def insert_many(collection, data_list):
        res = collection.insert_many(data_list)
        return res

    @staticmethod
    def find_one(collection, data, data_field={}): #查询数据
        if len(data_field):  # data_filed不为0
            res = collection.find_one(data, data_field)
        else:
            res = collection.find_one(data)
        return res

    @staticmethod
    def find_many(collection, data, data_field={}):
        if len(data_field):  #data_filed不为0
            res = collection.find(data, data_field)
        else:
            res = collection.find(data)
        return res
    '''
    Method: 更新一条文档数据
    parmes:
        collection:table name
        data_condition: 要修改数据的条件
        data_set: 修改数据的值
    '''
    @staticmethod
    def update_one(collection, data_condition, data_set):  # 表名，要修改的那一列，新数据
        res = collection.update_one(data_condition, data_set)
        return res

    @staticmethod
    def update_many(collection, data_condition, data_set):
        res = collection.update_many(data_condition, data_set)
        return res

    @staticmethod
    def delete_one(collection, data):
        return collection.delete_one(data)

    @staticmethod
    def delete_many(collection, data):
        return collection.delete_many(data)