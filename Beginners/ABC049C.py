s0 = input()

target = ['dream', 'dreamer', 'erase', 'eraser']

while True:
    len01 = len(s0)
    for i in range(4):
        s0 = s0.removesuffix(target[i])
    if len(s0) == len01:
        break
    else:
        pass

if s0 == '':
    print('YES')
else:
    print('NO')