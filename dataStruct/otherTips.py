# 2番目の要素でソート
from operator import itemgetter
l = [(1, 2), (3, 4), (5, 0)]
l.sort(key = itemgetter(1))



# dedaultdict: キーが存在しない場合に初期値を返す
# （通常の辞書ではエラーが発生する）
from collections import defaultdict
d = defaultdict(lambda: 100)    # 初期値を100に設定、括弧の中は関数

# 使用例
for i in range(10):
    d[i] = i * i
print(d[20])    # 100



# 累積和のリストを作成
# 数字のみならず文字列にも適用できる
from itertools import accumulate
num = [1, 3, 5, 7, 9]
str = ['ab', 'bc', 'cd']
cumnum = list(accumulate(num))  # [1, 4, 9, 16, 25]
cumstr = list(accumulate(str))  # ['ab', 'abbc', 'abbccd']



# 連続する同じ要素をグループ化
from itertools import groupby
bi = [0,0,0,1,1,0,0,0,1,1,0,1]
gr = groupby(bi)
for key, group in gr:
    print(f'{key}: {list(group)}')

# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0]
# 1: [1]
