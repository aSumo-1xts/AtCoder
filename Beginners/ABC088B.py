n   = int(input())
a0  = list(map(int,input().split()))
a1  = sorted(a0, reverse=True)

Alice, Bob = 0, 0
for i in range(n):
    if i%2 == 0: # 初回を含む偶数番目（0, 2, 4, ...）はAliceの得点
        Alice += a1[i]
    else:        # 奇数番目（1, 3, 5, ...）はBobの得点
        Bob += a1[i]

print(Alice - Bob)