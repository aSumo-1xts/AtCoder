div = 10//7     # 小数点以下の切り捨て
div = -(-10//7) # 小数点以下の切り上げ



from math import gcd
from functools import reduce

# 最大公約数
def my_gcd(numList):
    return reduce(gcd, numList)

# 最小公倍数
def my_lcm(numList):
    def lcm(x, y):
        return x*y // gcd(x, y)
    return reduce(lcm, numList)



# 素数判定
# for文で回せばエラトステネスの篩になる
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:  # 偶数で割る必要を無くしておく
        return False    
    else:           # 奇数の素数で割っていく
        for i in range(3, int(sqrt(n))+1, 2):
            if n%i == 0: return False
        return True



# 約数のリスト
from sortedcontainers import SortedSet
def divisor(n):
    i, s = 1, SortedSet()
    while i**2 <= n:
        if n%i == 0:
            s.add(i)
            s.add(n//i)
        i += 1
    return list(s)



# 素因数分解
from math import sqrt
def prime_factors(n):
    factors = []
    
    while n % 2 == 0:   # 2で割れるだけ割っておく
        factors.append(2)
        n //= 2
        
    # 奇数の素数で割っていく
    for i in range(3, int(sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
            
    # 最後に残った数が素数の場合、それも追加
    if n > 2: factors.append(n)
    return factors



# 1から10000までの累乗をすべて求めておいて、
# ピンポイントでnの累乗を知りたいときに引っ張り出してくる
# ただし mod p
def my_factorial(n):
    p       = 10**9 + 7
    sizeN   = 10000
    fact    = [1]
    for i in range(1, sizeN+1):
        fact.append(fact[-1] * i % p)
    return fact[n]