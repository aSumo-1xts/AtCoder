a0 = [int(input())]
a1 = str(a0[0])
l0 = list(a1)

b=0
for i in range(len(l0)):
    if l0[i] == '1':
        b += 1
    else:
        pass

print(b)