a = list(map(int,input().split()))
h = a[0]
w = a[1]
b = [list(input()) for _ in range(h)]
b.append(["." for _ in range(w)])

"""
h,wの最大値が50なので、全探索できる
"""

if b[0][0] == "#":
    if b[0][1]!="#" and b[1][0]!="#":
        print("No")
        exit()
    else:
        pass
else:
    pass

for i in range(1, h):
    if b[i][0] == "#":
        if b[i-1][0]!="#" and b[i][1]!="#" and b[i+1][0]!="#":
            print("No")
            exit()
        else:
            pass
    else:
        pass

for i in range(1, w):
    if b[0][i] == "#":
        if b[0][i-1]!="#" and b[1][i] != "#" and b[0][i+1] != "#":
            print("No")
            exit()
        else:
            pass
    else:
        pass

for i in range(1, h):
    for j in range(1, w):
        if b[i][j] == "#":
            if b[i-1][j] != "#" and b[i+1][j] != "#" and b[i][j-1] != "#" and b[i][j+1] != "#":
                print("No")
                exit()
            else:
                pass
        else:
            pass

print("Yes")