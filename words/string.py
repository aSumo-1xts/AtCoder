import re
s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

# 正規表現パターンとマッチングする部分を抽出
print(re.match(r'([a-z]+)@([a-z]+)\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

# 正規表現パターンとマッチングする部分を置換
print(re.sub(r'([a-z]+)@([a-z]+)\.com', 'replaced@adress.com', s))
# replaced@adress.com bbb@yyy.net ccc@zzz.org