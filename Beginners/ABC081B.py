n = int(input())
a = list(map(int,input().split()))

res = 0
j = True
b0 = [0] * n
c0 = [0] * n
while j==True:
    for i in range(n):
        b0[i] = a[i]//2
        c0[i] = a[i]%2
        a[i]  = b0[i]
        if c0[i] != 0:
            j = False
            break
        else:
            pass
    res += 1

res -= 1
print(res)