# ﻿如何进行反向迭代以及如何实现反向迭代


# 对列表进行反向迭代
# 第一种方式：使用reverse()函数
l = [1, 2, 3, 4, 5]
l.reverse()
print(l)

# 第二种方式：使用切片操作
l = [1, 2, 3, 4, 5]
a = l[::-1]
print(a)

# 第三种方式：内置的反向迭代器
l = [1, 2, 3, 4, 5]
for i in reversed(l):
    print(i, end="")

print()
print("-" * 20)


# 对自定义类型进行反向迭代
class FloatNum():
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for i in reversed(FloatNum(1, 10, 2)):
    print(i)
