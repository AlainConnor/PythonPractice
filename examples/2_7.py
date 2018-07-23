# 如何实现用户历史记录功能

from collections import deque

q = deque([], 5)
while True:
    t = input("input:")
    if t == 'quit':
        break
    q.append(t)
    print(q)

