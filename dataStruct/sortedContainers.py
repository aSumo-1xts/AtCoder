'''
sortedcontainers: sorted containers
ソート状態を保ったまま、要素の追加・削除を高速に実行できるデータ構造たち

これを使えない場合はAVL木が有効っぽい
https://stnkien.hatenablog.com/entry/avl-tree

各処理時の計算量は原則としてO(logN)で一定
min, max関数はiterableによって走査され計算量O(N)となるため使用しないこと
'''

from sortedcontainers import SortedSet, SortedList, SortedDict



'''
SortedSet: 常にソートされている集合
'''
# 生成
s = SortedSet([3, 1, 4, 1, 5, 9, 2, 6, 5])  # 初期化時の計算量はO(NlogN)


# 操作メソッド
s.add(7)        # 7を追加
s.add(5)        # 既に含まれている場合は無視される
s.discard(4)    # 3を削除
s.discard(100)  # 存在しない場合は無視される
s.remove(100)   # こっちはKeyErrorが返される
s.pop()         # 末尾（最大の要素）を取り出して削除
s.pop(0)        # 先頭（最小の要素）を取り出して削除、計算量は変わらずO(logN)


# 取得メソッド
len(s)  # 集合の要素数を取得
s[2]    # 3番目の要素を取り出す
s[1:3]  # スライスも普通に使える、計算量は長さKに対してO(KlogN)
s.index(3)      # 3の最小インデックス（最初の出現位置）を返す
s.index(100)    # 存在しない場合はValueErrorを返す
s.irange(3, 5)  # 3以上5以下の範囲の要素をイテレート（列挙）する

s.bisect_left(3)    # 二分探索で3を挿入するべき位置を返す
s.bisect_right(3)   # 上に同じ、既に存在する場合は右隣を返す

list(s) # 全要素を素直に出力したいときはリスト化する


'''
SotedList: 常にソートされているリスト
SortedSetとほぼ同じメソッドを持つが、要素の重複を許す
'''
# 生成
l = SortedList([3, 1, 4, 1, 5, 9, 2, 6, 5])  # 初期化時の計算量はO(NlogN)

# 操作メソッド
l.add(7)        # 7を追加
l.add(5)        # 既に含まれている場合は無視される
l.discard(4)    # 3を削除
l.discard(100)  # 存在しない場合は無視される
l.remove(100)   # こっちはKeyErrorが返される
l.pop()         # 末尾（最大の要素）を取り出して削除
l.pop(0)        # 先頭（最小の要素）を取り出して削除、計算量はO(logN)のまま


# 取得メソッド
len(l)  # リストの要素数を取得
l[2]    # 3番目の要素を取り出す
l[1:3]  # スライスも普通に使える、計算量は長さKに対してO(KlogN)
l.index(3)      # 3の最小インデックス（最初の出現位置）を返す
l.index(100)    # 存在しない場合はValueErrorを返す
l.count(3)      # 3の個数を返す（SortedSetにもあるけど意味がない）
l.irange(3, 5)  # 3以上5以下の範囲の要素をイテレート（列挙）する

l.bisect_left(3)    # 二分探索で3を挿入するべき位置を返す
l.bisect_right(3)   # 上に同じ、既に存在する場合は右隣を返す



'''
SortedDict: 常にソートされている辞書
'''
# 生成
d = SortedDict({'c': 2, 'a': 1, 'd': 3, 'b': 4})
# {'a': 1, 'b': 4, 'c': 2, 'd': 3}  # keyの昇順にソートされる


# 操作メソッド（普通の辞書と同じ）
d.items()   # [('a', 1), ('b', 4), ('c', 2), ('d', 3)]
d.keys()    # ['a', 'b', 'c', 'd']
d.values()  # [1, 4, 2, 3]
d.pop()     # 末尾の要素を削除、そのvalueを取り出す
d.pop(0)    # 先頭の要素を削除、そのvalueを取り出す。計算量はO(logN)のまま


# 取得メソッド
d['a']    # 'a'のvalueを取り出す
'c' in d  # True