# -*- coding:utf-8 -*-

import pickle
print("序列化：")
print("将一个对象序列化，然后写入文件：")
d = dict(name='Bob', age=20, score=88)
dBytes = pickle.dumps(d) #dumps方法吧任意对象序列化成bytes。
print(dBytes)

#这是第一种写入：
#with open('d:/testFile.txt','wb') as f:
#    f.write(dBytes)

#这是第二种写入：
try:
    f = open('d:/testFile.txt','wb')
    pickle.dump(d, f) # 注意，这里是dump，而上面的是dumps
except Exception as e:
    print(e)
finally:
    f.close()

#
print("将对象从磁盘读到内存中：")
try:
    f = open('d:/testFile.txt','rb')
    d = pickle.load(f)
    print(d)
except Exception as e:
    print(e)
finally:
    f.close()

#
print("将对象转成json：")
import json
d = dict(name='Bob', age=20, score=88)
jsonRes = json.dumps(d)
print(jsonRes)

#
print("将自定义类转成json：")
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
s = Student('ZhangSan',18,88)
#print(json.dumps(s)) # 这里直接报错，Student不是一个可序列化的对象。

#解决办法一：添加一个转换函数
def studnet2dict(std):
    return {
        "name":std.name,
        "age":std.age,
        "score":std.score
    }
print(json.dumps(s, default=studnet2dict))

#解决办法二：调用特殊属性
print( json.dumps(s, default=lambda obj:obj.__dict__) )

#
print("json反序列化：")
def dict2studnet(d):
    return Student(d['name'],d['age'],d["score"])

jsonStr = '{"name":"Lisi","age":"28","score":"100"}'
s = json.loads(jsonStr, object_hook=dict2studnet)
print(s.name,s.age,s.score)











