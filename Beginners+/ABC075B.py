a = list(map(int,input().split()))
h = a[0]
w = a[1]
b = [list(input()) for _ in range(h)]

# 入力を読みながら、出力用のものを新たに作成する
# 縦横ともに一つ大きめに作って、範囲外参照を回避
ans = [[0]*(w+1) for _ in range(h+1)]

# H, Wともに最大で50程度なので、全探索して良い

# 言わば原点
if b[0][0] == "#":
    ans[0][1] +=1
    ans[1][1] +=1
    ans[1][0] +=1
else:
    pass

# 一列目の処理
for i in range(1, h):
    if b[i][0] == "#":
        ans[i-1][0] +=1
        ans[i-1][1] +=1
        ans[i][1]   +=1
        ans[i+1][0] +=1
        ans[i+1][1] +=1
    else:
        pass

# 一行目の処理
for j in range(1, w):
    if b[0][j] == "#":
        ans[0][j-1] +=1
        ans[0][j+1] +=1
        ans[1][j]   +=1
        ans[1][j-1] +=1
        ans[1][j+1] +=1
    else:
        pass

# それ以外の処理
for i in range(1, h):
    for j in range(1, w):
        if b[i][j] == "#":
            ans[i-1][j-1]   +=1
            ans[i-1][j]     +=1
            ans[i-1][j+1]   +=1
            ans[i][j-1]     +=1
            ans[i][j+1]     +=1
            ans[i+1][j-1]   +=1
            ans[i+1][j]     +=1
            ans[i+1][j+1]   +=1
        else:
            pass

# 出力
for i in range(h):
    for j in range(w):
        if b[i][j] == "#":
            ans[i][j] = "#"
        else:
            ans[i][j] = str(ans[i][j])
        print(ans[i][j], end='')
    print()