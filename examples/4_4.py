# ﻿如何将多个小字符串拼接成一个大的字符串

strList = ["123", "abc", "def"]

# 对列表中的项进行迭代，用+号实现
t = ""
for i in strList:
    t += i

print(t)

# 使用join()方法
print("".join(strList))

# 如果列表中含整形变量
strList1 = ["123", "abc", "def", 456]
print("".join([str(i) for i in strList]))
print("".join(i for i in strList))
