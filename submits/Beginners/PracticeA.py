a0 = [int(input()) for _ in range(1)]
a1 = list(map(int,input().split()))
b0 = [input() for _ in range(1)]

sum = a0[0] + a1[0] + a1[1]

print(f'{sum} {b0[0]}')