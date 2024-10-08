# 中国剰余定理:
# 3で割ると2余り、5で割ると3余り、7で割ると2余る。
# この条件を満たす正の整数のうち、最小のものを求めよ。

# 的なやつに使える（末尾に実行例あり）



def inv_gcd(a,b):
    a %= b
    if a==0: return (b, 0)
    
    s, t, m0, m1 = b, a, 0, 1
    
    while t:
        u   = s//t
        s  -= t*u
        m0 -= m1*u
        s, t, m0, m1 = t, s, m1, m0

    if m0<0: m0 += b//s
    return (s, m0)



def crt(r, m):
    assert len(r)==len(m)
    n       = len(r)
    r0, m0  = 0, 1
    
    for i in range(n):
        assert 1<=m[i]
        r1, m1 = r[i]%m[i], m[i]
        
        if m0<m1: r0, r1, m0, m1 = r1, r0, m1, m0
        if m0%m1==0:
            if r0%m1!=r1: return (0, 0)
            continue
        
        g, im   = inv_gcd(m0, m1)
        u1      = m1//g
        if (r1-r0)%g: return (0, 0)
        
        x   = (r1-r0)//g % u1 * im % u1
        r0 += x*m0
        m0 *= u1
        if r0<0: r0 += m0
    
    return (r0, m0)



C = [3, 5, 7]
R = [2, 3, 2]

r, m = crt(R, C)
print(r)