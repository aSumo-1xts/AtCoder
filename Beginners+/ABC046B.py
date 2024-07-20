a = list(map(int,input().split()))

n = a[0] # ボールの個数     1~1000
k = a[1] # ペンキの色の数   2~1000

ans = 1

for i in range(n):
    if i == 0:
        ans *= k
    else:
        ans *= (k-1)

print(ans)