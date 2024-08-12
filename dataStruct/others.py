# 2番目の要素でソート
from operator import itemgetter
l = [(1, 2), (3, 4), (5, 0)]
l.sort(key = itemgetter(1))