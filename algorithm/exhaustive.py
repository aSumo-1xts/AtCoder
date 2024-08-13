# 深さ優先探索
def dfs(v, p):
    # g = []
    # for u in g[v]:
    #     if u == p:
    #         continue
    #     dfs(u, v)
    # return

# 幅優先探索
from collections import deque
def bfs(v):
        # q = deque([v])
        # g = []
        # while q:
        #     v = q.popleft()
        #     for u in g[v]:
        #         if u == p:
        #             continue
        #         q.append(u)
        # return