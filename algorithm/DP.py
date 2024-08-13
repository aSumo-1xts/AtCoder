# 桁DP
# A以下B以上の非負整数のうち、「Xが付くまたはXの倍数」かつ「Yの倍数でない」数の総数を求める例
from itertools import product
from collections import defaultdict
def digitDP(a, b):
    X = 3   # Xがつく or Xの倍数
    Y = 8   # Yの倍数でない
    
    def count(x):
        a   = str(x)
        n   = len(a)
        dp  = defaultdict(int)
        dp[0, 0, 0, 0, 0] = 1

        for i, less, hasX, modX, modY in product(range(n), (0,1), (0,1), range(X), range(Y)):
            max_d = 9 if less else int(a[i])
            for d in range(max_d+1):
                less_ = less or d < max_d
                hasX_ = hasX or d == X
                modX_ = (modX + d) % X
                modY_ = (modY*10 + d) % Y
                dp[i + 1, less_, hasX_, modX_, modY_] += dp[i, less, hasX, modX, modY]

        criteria = ((n, less, hasX, modX, modY) for less, hasX, modX, modY \
            in product((0, 1), (0,1), range(X), range(Y)) if (hasX or modX==0) and modY!=0)
        return sum(dp[c] for c in criteria)

    return count(b) - count(a-1)