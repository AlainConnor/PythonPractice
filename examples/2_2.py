# 如何为元组中的每个元素命名, 提高程序可读性
from collections import namedtuple

NAME = 0
AGE = 1
SEX = 2
# 可替换的更为简单的语法
# NAME, AGE, SEX, EMAIL = range(4)
student = ('Jim', 16, 'male', 'jim@gmail.com')

# name
print("name:", student[NAME])
# age
print("age:", student[AGE])
# sex
print("sex:", student[SEX])

print("--------------------------------------------------------------")
print("使用namedtuple对象")
# 实例化namedtuple对象
student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s1 = student('Jim', 16, 'male', 'jim@gmail.com')  # 使用student来创建一个元组,按顺序传值
print(s1)
s2 = student(name='Bob', age=20, sex='female', email='bob@gmail.com')  # 关键字传值
print("属性方式访问：", s2.name, s2.age)
print("数组关键字索引访问：", s2.name, s2.age)

# 判断s1是否为tuple的子类
print(isinstance(s1, tuple))
