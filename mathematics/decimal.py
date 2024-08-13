# 10進数をn進数に変換
def deci2n(X, n):
    return deci2n(X//n, n) + str(X%n) if X//n else str(X%n)

# n進数を10進数に変換
def n2deci(X, n):
    X = str(X)
    return sum([int(X[i]) * n**(len(X)-i-1) for i in range(len(X))])

# a進数をb進数に変換
def n2n(X, a, b):
    return n2deci(deci2n(X, a), b)