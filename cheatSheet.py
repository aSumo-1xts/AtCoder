# 何も考えずに使う
import sys
input = sys.stdin.readline

# 2番目の要素でソート
from operator import itemgetter
l = [(1, 2), (3, 4), (5, 0)]
l.sort(key = itemgetter(1))
print(l)
print()

# 直積
from itertools import product
# その1
for t in product([1, 2, 3], ['a', 'b']):
    print(t)
print()
# その2
for t in product(['a', 'b'], repeat=3):
    print(''.join(t))
print()

# 順列
from itertools import permutations
for t in permutations(['a', 'b', 'c']):
    print(t)
print()

# 重複なし組み合わせ
from itertools import combinations
for t in combinations(['a', 'b', 'c'], 2):
    print(t)
print()

# 重複あり組み合わせ
from itertools import combinations_with_replacement
for t in combinations_with_replacement(['a', 'b', 'c'], 2):
    print(t)
print()
