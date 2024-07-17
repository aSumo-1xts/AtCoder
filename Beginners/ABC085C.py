def culc(i, j, k):
    return i*10 + j*5 + k*1

a0 = list(map(int,input().split()))

n = a0[0]
y = a0[1]//1000

i, j, k = 0, 0, 0
if n*10 < y:
    print(-1, -1, -1)
    exit()
elif n*10 == y:
    print(n, 0, 0)
    exit()
else:
    for i in range(n+1):
        for j in range(n-i+1):
            k = n-i-j
            if culc(i, j, k) == y:
                print(i, j, k)
                exit()
            elif culc(i, j, k) > y:
                break
            else:
                pass

print(-1, -1, -1)