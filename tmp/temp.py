# 临时文件

l = {i for i in range(3)}
print(type(l))

l1 = iter(l)
for i in l1:
    print(i)

l2 = iter(l)
for i in l2:
    print(i)
