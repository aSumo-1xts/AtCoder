input = list(map(int,input().split()))

a = input[0]
b = input[1]
x = input[2]

t = 0

if a%x == 0:
    first = a
else:
    first = a + x - a%x

if b%x == 0:
    last = b
else:
    last = b - b%x

res = (last - first)//x + 1
print(res)

# なるほどね～～～