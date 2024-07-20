n = int(input())
s = list(input())

w, e = [0]*(n+1), [0]*(n+1)     # ちゃんと定義しよう
cntW, cntE = 0, 0
for i in range(n):      # 累積和を求めておく
    if s[i] == "W":
        w[i]  = cntW    # i時点でのWの数
        e[i]  = cntE    # i時点でのEの数
        cntW += 1
    else:
        w[i]  = cntW    # i時点でのWの数
        e[i]  = cntE    # i時点でのEの数
        cntE += 1
w[n], e[n] = cntW, cntE

best = n
for l in range(n):      # リーダーはlにいる人
    cnt = w[l] + (e[n]-e[l+1])
    # 範囲外参照回避のためには、大きくとるのが一番
    if cnt < best:
        best = cnt
    else:
        pass

print(best)