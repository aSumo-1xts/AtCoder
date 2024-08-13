from collections import defaultdict
import heapq
class Dijkstra():
    def __init__(self):
        self.e = defaultdict(list)

    def add(self, u, v, d, directed=False):
        """
        #0-indexedでなくてもよいことに注意
        #u = from, v = to, d = cost
        #directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u].append([v, d])
            self.e[v].append([u, d])
        else:
            self.e[u].append([v, d])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        #0-indexedでなくてもよいことに注意
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        d       = defaultdict(lambda: float('inf'))
        prev    = defaultdict(lambda: None)
        d[s]    = 0
        q       = []
        
        heapq.heappush(q, (0, s))
        v = defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]: continue
            v[u] = True
            for uv, ud in self.e[u]:
                if v[uv]: continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv]       = vd
                    prev[uv]    = u
        return d, prev

    def getDijkstraShortestPath(self, start, goal):
        _, prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]



class BellmanFord():
    def __init__(self, N):
        self.N = N
        self.edges = []

    def add(self, u, v, d, directed=False):
        """
        u = from, v = to, d = cost
        directed = Trueのとき、有向グラフである。
        """
        if directed is False:
            self.edges.append([u, v, d])
            self.edges.append([v, u, d])
        else:
            self.edges.append([u, v, d])

    def BellmanFord_search(self, s):
        """
        :param s: 始点
        :return: d[i] 始点sから各点iまでの最短経路
        """
        d           = [float('inf') for i in range(self.N)]
        d[s]        = 0
        numEdges    = len(self.edges)
        while True:
            update = False
            for i in range(numEdges):
                e = self.edges[i]
                # e: 辺iについて [from,to,cost]
                if d[e[0]] != float("inf") and d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    update  = True
            if not update: break
        return d

    def BellmanFord_negative_bool(self, start, numNodes):
        # 負の閉路の検出, Trueなら負の閉路が存在する
        d = [float('inf') for i in range(self.N)]
        d[start] = 0
        numEdges = len(self.edges)
        for i in range(numNodes):
            for j in range(numEdges):
                e = self.edges[j]
                if d[e[1]] > d[e[0]] + e[2]:
                    d[e[1]] = d[e[0]] + e[2]
                    if i == numNodes-1:
                        return True, d
        return False, d



import heapq
class Prim():
    # 無向グラフであるという前提に注意
    def __init__(self, N):
        self.edge = [[] for i in range(N)]
        self.N = N

    def add(self, u, v, d):
        """
        u = from, v = to, d = cost
        0-indexedであることに注意、graph.add(u-1, v-1)とする必要がある
        """
        self.edge[u].append([d, v])  # コスト、e_toとなっていることに注意
        self.edge[v].append([d, u])

    def delete(self, u, v):
        self.edge[u] = [_ for _ in self.edge[u] if _[0] != v]
        self.edge[v] = [_ for _ in self.edge[v] if _[0] != u]

    def Prim(self):
        """
        return: 最小全域木のコストの和
        """
        used        = [True] * self.N  # True:不使用
        edgelist    = []
        for e in self.edge[0]:
            heapq.heappush(edgelist, e)
        
        used[0] = False
        res = 0
        while len(edgelist) != 0:
            minedge = heapq.heappop(edgelist)
            if not used[minedge[1]]: continue
            v = minedge[1]
            used[v] = False
            for e in self.edge[v]:
                if used[e[1]]: heapq.heappush(edgelist, e)
            res += minedge[0]
        return res



class Kruskal_UnionFind():
    # 無向グラフであるという前提に注意
    def __init__(self, N):
        self.edges = []
        self.rank = [0] * N
        self.par = [i for i in range(N)]
        self.counter = [1] * N

    def add(self, u, v, d):
        """
        u = from, v = to, d = cost
        """
        self.edges.append([u, v, d])

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            z = self.counter[x] + self.counter[y]
            self.counter[x], self.counter[y] = z, z
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def size(self, x):
        x = self.find(x)
        return self.counter[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def Kruskal(self):
        """
        return: 最小全域木のコストの和
        """
        edges = sorted(self.edges, key=lambda x: x[2])  # costでself.edgesをソートする
        res = 0
        for e in edges:
            if not self.same(e[0], e[1]):
                self.unite(e[0], e[1])
                res += e[2]
        return res



class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)] for i in range(N)]
        # d[u][v] : 辺uvのコスト(存在しないときはinf)

    def add(self, u, v, c, directed=False):
        """
        0-indexedであることに注意
        u = from, v = to, c = cost
        directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.d[u][v] = c
            self.d[v][u] = c
        else:
            self.d[u][v] = c

    def WarshallFloyd_search(self):
        # これを d[i][j]: iからjへの最短距離 にする
        # 本来無向グラフでのみ全域木を考えるが、二重辺なら有向でも行けそう
        # d[i][i] < 0 なら、グラフは負のサイクルを持つ
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(
                        self.d[i][j], self.d[i][k] + self.d[k][j])
        hasNegativeCycle = False
        for i in range(self.N):
            if self.d[i][i] < 0:
                hasNegativeCycle = True
                break
        for i in range(self.N):
            self.d[i][i] = 0
        return hasNegativeCycle, self.d