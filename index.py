# 应用层
from db_user import DBUser

user = DBUser()  # 初始化
res = user.find_one({"name":"董明珠"})
print(res)

res = user.find_one({"name":"董明珠"},{"_id":0})
print(res)