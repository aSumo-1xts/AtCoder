a0 = int(input())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))

candies = 0
for i in range(a0):         # 下段へ行くタイミングはi
    candy = 0
    
    for j in range(0, i+1): # 1段目の足し算
        candy += a1[j]
    for k in range(i, a0):  # 2段目の足し算（続き）
        candy += a2[k]
    
    if candy > candies:
        candies = candy

print(candies)