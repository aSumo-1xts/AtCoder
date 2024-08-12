n = int(input())
a = [int(input()) for _ in range(n)]
a.insert(0, 0)  # Insert 0 to make the indices start from 1

i, cnt = 1, 1
collection = {a[0]}  # Use a set instead of a list
while True:
    if a[i] == 2:
        print(cnt)
        exit()
    elif a[i] in collection:
        print(-1)
        exit()
    else:
        collection.add(a[i])  # Use add() method to add elements to the set
        i = a[i]
        cnt += 1
        if cnt > n:
            print(-1)
            exit()

# "more rapid"は強し…
# listよりもsetの方が要素の検索が早く、計算量を減らせるので積極的に活用しよう
# setに要素を追加する際にはappend()ではなくadd()を使う