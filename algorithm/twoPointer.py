# 尺取り法:
# 長さNの数列Aについて、要素の和がK以上となる部分列の数を求める例
def twoPointer(N, K, A):
    ans = 0
    t = 0
    j = 0
    for i in range(N+1):
        while j < N and t < K:
            t += A[j]
            j += 1
        if t >= K:
            ans += N-j+1
        if i == N:
            break
        t -= A[i]
    print(ans)