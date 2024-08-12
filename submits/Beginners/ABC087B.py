def culc(s, t, u):
    return (s*10 + t*2 + u*1)

a0 = [int(input()) for _ in range(4)]
a1 = [culc(a0[0], a0[1], a0[2]), a0[3]//50] # 単位を揃える

c = 0
if a1[1] > a1[0]:
    print(0)
elif a1[1] == a1[0]:
    print(1)
else:
    for i in range(a0[0]+1):
        for j in range(a0[1]+1):
            for k in range(a0[2]+1):
                if culc(i, j, k) < a1[1]:
                    pass
                elif culc(i, j, k) == a1[1]:
                    c += 1
                else:
                    break
    print(c)

# 何も考えずに多重forで良いらしい