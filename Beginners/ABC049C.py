s0 = input()

target = ['dream', 'dreamer', 'erase', 'eraser']

while True:
    len01 = len(s0)
    for i in range(4):
        s0 = s0.removesuffix(target[i]) # 後ろからほどく
    if len(s0) == len01:                # 文字列の変化を長さで確認
        break
    else:
        pass

if s0 == '':
    print('YES')
else:
    print('NO')