input = list(map(int,input().split()))

a = input[0]    # 1~100
b = input[1]    # 1~100
c = input[2]    # 0~B

# a%b=c
a0 = a

i = 1
while True:
    if a%b == c:
        print("YES")
        break
    elif i>b:   # 何回繰り返してから諦めるか？
        print("NO")
        break
    else:
        i += 1
        a = i*a0