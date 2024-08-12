'''
deque（デック）: double-ended queue
両端からの要素の追加・削除を高速に実行できるキューの一種
'''

from collections import deque   # 標準データ構造ではないことに留意



# 生成
d = deque([1, 2, 3])


# 操作メソッド
d.append(4)             # 末尾に4を追加
d.appendleft(0)         # 先頭に0を追加
last = d.pop()          # 末尾の要素を削除しながら取り出す
first = d.popleft()     # 先頭の要素を削除しながら取り出す
d.extend([5, 6])        # 末尾に複数の要素を追加
d.extendleft([-1, 0])   # 先頭に複数の要素を追加
d.insert(3, 3.5)        # 前から4番目に3.5を挿入
d.insert(-1, 5.5)       # 後から2番目に5.5を挿入
d.rotate(1)             # 右に1つずつスクロールされる
d.rotate(-2)            # 左に2つずつスクロールされる


# 取得メソッド
d[2]        # 3番目の要素を取り出す
# d[2:4]            # TypeError: よくあるスライスは使えない
import itertools    # 代わりにitertools.isliceを使う
deque(itertools.islice(d, 2, 4))

len(d)      # 要素数を返す
d.index(3)  # 3の最小インデックス（最初の出現位置）を返す
d.count(3)  # 3の個数を返す
3 in d      # 3が含まれているかどうかを返す
d.copy()    # コピーを返す
d.clear()   # 全要素を削除


# 上限付き生成
d = deque([1, 2, 3], maxlen=3)  # 要素数の上限付きdequeを作成
d.append(4)                     # 上限を超えると逆側から削除される