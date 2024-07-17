def culc(n):
    s = n//10000 # 万の位
    t = (n%10000)//1000 # 千の位
    u = ((n%10000)%1000)//100 # 百の位
    v = (((n%10000)%1000)%100)//10 # 十の位
    w = (((n%10000)%1000)%100)%10 # 一の位
    return s+t+u+v+w

a = list(map(int,input().split()))

c = 0
for i in range(1, a[0]+1):
    if a[1] <= culc(i) <= a[2]:
        c += i
    else:
        pass

print(c)