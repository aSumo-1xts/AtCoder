num = int(input())

val = 1
for i in range(2,num+1):
    val *= i
    if val > 1.0e+9:
        val %= 1.0e+9 + 7

print(int(val))