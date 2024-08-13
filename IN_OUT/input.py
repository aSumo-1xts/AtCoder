# 何も考えずに使う
import sys
input = sys.stdin.readline


# 1個の整数
n = int(input().split())

# 2個の整数たち
a, b = map(int, input().split())

# 1行の整数たち
a = list(map(int, input().split()))

# 複数行の整数たち
a = [int(input().split()) for _ in range(n)]


# 1行の文字列たち
s = input().split()

# 複数行の文字列たち
s = [input().split() for _ in range(n)]


# 1個の文字列を一文字ずつに分解して格納
c = list(input().split())

# 複数行の文字列を一文字ずつに分解して格納
c = [list(input().split()) for _ in range(n)]
# 再結合するとき
C = ''.join(map(str, c))