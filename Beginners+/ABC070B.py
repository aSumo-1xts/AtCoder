a = list(map(int,input().split()))
A0, A1, B0, B1 = a[0], a[1], a[2], a[3]

# 時系列
s = sorted([A0, A1, B0, B1])

if s[0] == A0:
    if s[1] == A1:
        res = 0
    else:
        if s[2] == A1:
            res = A1-B0
        else:
            res = B1-B0
else:
    if s[1] == B1:
        res = 0
    else:
        if s[2] == B1:
            res = B1-A0
        else:
            res = A1-A0

print(res)