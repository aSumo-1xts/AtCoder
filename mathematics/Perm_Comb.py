# 直積1: 複数のリストから1つずつ要素を選んで組にしたものを列挙
# 小学校の縦割り班の究極形
def make_group(ll): # 「リストのリスト」を引数に取る
    from itertools import product
    ans = []
    for t in product(*ll):
        ans.append(t)
    return ans



# 直積2: リストlから要素を自由に選んで、n個並べたものを列挙
# 2進数n桁のビット全探索に使える
def bit_search(l, n):
    from itertools import product
    ans = []
    for t in product(l, repeat=n):
        ans.append(t)
    return ans



# 順列: リストlのすべての並べ方を列挙
# 入力するリスト長は5程度に留めること
def perm(l):
    from itertools import permutations
    ans = []
    for t in permutations(l):
        ans.append(t)
    return ans



# 重複あり組み合わせ: nPrを列挙
def nPr_bin(nP, r):
    from itertools import combinations_with_replacement
    ans = []
    for t in combinations_with_replacement(nP, r):
        ans.append(t)
    return ans



# 重複なし組み合わせ: nCrを列挙
def nCr_bin(nC, r):
    from itertools import combinations
    ans = []
    for t in combinations(nC, r):
        ans.append(t)
    return ans



# 重複なし組み合わせ: nCrそのものの値を計算
# ただし mod p
def nCr(n, r):
    
    def culc(N, R, P):
        if R<0 or N<R: return 0
        R = min(R, N-R)
        return fact[N] * factinv[R] * factinv[N-R] % P

    sizeN   = 10000     # 適宜変更
    p       = 10**9 + 7 # よくあるのはこの値
    fact    = [1, 1]    # fact[n] = (n! mod p)
    factinv = [1, 1]    # factinv[n] = ((n!)^(-1) mod p)
    inv     = [0, 1]    # factinv 計算用

    for i in range(2, sizeN+1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)
    
    return culc(n, r, p)