# 如何让字典保持有序

from collections import OrderedDict
from time import time
from random import randint
d = OrderedDict()
people = list("ABCDEFGH")

start = time()
for i in range(len(people)):
    input()
    p = people.pop(randint(0, len(people) - 1))
    end = time()
    print(i +1 , p, end - start, end="")
    d[p] = (i + 1, end - start)

print()
print("*"*20)
for k in d:
    print(k, d[k])


