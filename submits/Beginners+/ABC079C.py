input = list(input())
a = int(input[0])
b = int(input[1])
c = int(input[2])
d = int(input[3])

def pm(num):
    if num%2 == 1:
        return -1
    else:
        return 1

def pm_str(num):
    if num%2 == 1:
        return '-'
    else:
        return '+'

for j in range (2):
    for k in range (2):
        for l in range (2):
            res = a + pm(j)*b + pm(k)*c + pm(l)*d
            if res == 7:
                word = str(a) + pm_str(j) + str(b) + pm_str(k) + str(c) + pm_str(l) + str(d) + '=7'
                print(word)
                exit()
            else:
                pass

# シンプルに総当たりで良い