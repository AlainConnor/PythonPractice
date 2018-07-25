# 如何使用生成器函数实现可迭代对象


class PrimeNum():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrime(self, k):
        if k < 2:
            return False

        for i in range(2, k):
            if k % i == 0:
                return False

        return True

    def __iter__(self):
        for i in range(self.start, self.end+1):
            if self.isPrime(i):
                yield i


for x in PrimeNum(0, 100):
    print(x)

