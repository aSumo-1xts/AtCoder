n   = int(input())
a0  = [int(input()) for _ in range(n)]
print(len(list(set(a0))))

# set関数は重複を削除してくれる
# リストに変換して長さを取得