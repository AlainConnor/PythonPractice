# ﻿如何在一个for语句循环中迭代多个可迭代对象
from random import randint

# 原始方式
chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]
total1 = []
for i in range(len(chinese)):
    total1.append(chinese[i] + math[i] + english[i])
print(total1)

# 并行方式
total2 = []
for c, m, e in zip(chinese, math, english):
    total2.append(c + m + e)
print(total2)

# 串行方式
from itertools import chain

e1 = [randint(60, 100) for _ in range(30)]
e2 = [randint(60, 100) for _ in range(35)]
e3 = [randint(60, 100) for _ in range(25)]
count = 0
for i in chain(e1, e2, e3):
    if i >= 90:
        count += 1
print(count)

