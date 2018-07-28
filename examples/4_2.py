# ﻿如何判断字符串a是否以字符串b开头或结尾

listdir = ["a.cpp", "b.java", "c.py", "d.c", "f.sh", "h.cpp"]

# 输出所有cpp文件
cpplist = [i for i in listdir if i.endswith(".cpp")]
print(cpplist)

# 输出所有cpp文件或py文件
cppORpylist = [i for i in listdir if i.endswith((".cpp", ".py"))]
print(cppORpylist)