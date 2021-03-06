'''
mongodb_base 用来和MongoDB链接的信息
db_base 操作所有数据库的公共方法，其他db继承该类，子类继承或者个性化操作数据库的方法
mongodb_operation 静态方法和MongoDB进行交互
'''


'''1.1封装 数据库链接'''
from pymongo import MongoClient

#连接数据库
class MC(object):  # 最好把object加上
    def __init__(self):  # 自带return
        self.client = MongoClient('127.0.0.1',27017)
        self.db = self.client.py08db