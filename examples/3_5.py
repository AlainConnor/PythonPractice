# 如何对迭代器进行切片操作

# 使用内置readlines()函数
f = open("../tmp/CodingStyle.txt")
text = f.readlines()
for i in text[100:110]:
    print(i)

print()
print("-"*60)

# 使用库函数
from itertools import islice
f = open("../tmp/CodingStyle.txt")
for i in islice(f, 100, 110):
    print(i)

