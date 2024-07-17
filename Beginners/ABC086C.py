def calc(distance, time):
    if distance > time: # 遠すぎる場合
        return False
    elif distance%2 != time%2:
        return False
    else:
        return True

n = int(input())
txy = [map(int, input().split()) for _ in range(n)]
t, x, y = [list(i) for i in zip(*txy)]

# 奇数マス離れた場所へは奇数回(t)でしか移動できない
# 偶数マス離れた場所へは偶数回(t)でしか移動できない

distance = abs(x[0]) + abs(y[0])
time = t[0]
if calc(distance, time)==False:
    print("No")
    exit()
else:
    pass

for i in range(1, n):
    distance = abs(x[i]-x[i-1]) + abs(y[i]-y[i-1])
    time = t[i]-t[i-1]
    if calc(distance, time)==False:
        print("No")
        exit()
    else:
        pass

print("Yes")