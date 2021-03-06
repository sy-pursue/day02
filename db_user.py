from db_base import DBBase

# 继承DBBase类个性化，这个类是专门用来操作 pyuser 集合的。有几个表就可以创建几个类
class DBUser(DBBase):
    def __init__(self):
        super(DBUser,self).__init__("pyuser")  # 使用super初始化父类