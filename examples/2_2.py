from collections import namedtuple
# 如何为元组中的每个元素命名, 提高程序可读性
NAME = 0
AGE = 1
SEX = 2
NAME, AGE, SEX, EMAIL = range(4)
student = ('Jim', 16, 'male', 'jim@gmail.com')
# name
print(student[NAME])
# age
print(student[AGE])
# sex
print(student[SEX])

student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s1 = student('Jim', 16, 'male', 'jim@gmail.com')
print(s1)
s2 = student(name='Bob', age=20, sex='female', email='bob@gmail.com')
print(s2.name)
print(s2.age)

print(isinstance(s1, tuple))
