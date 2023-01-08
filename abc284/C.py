class unionfind:
    def __init__(self,n):
        self.n = n
        self.par = [-1]*(n+1)
        self.size = [1]*(n+1)
    
    def root(self,x):
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    def unit(self,u,v):
        rootu = self.root(u)
        rootv = self.root(v)
        if rootu != rootv:
            if self.size[rootu] < self.size[rootv]:
                self.par[rootu] = rootv
                self.size[rootv] += self.size[rootu]
            else:
                self.par[rootv] = rootu
                self.size[rootu] += self.size[rootv]
    
    def same(self,u,v):
        return self.root(u) == self.root(v)

N,M = map(int, input().split())
point = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int, input().split())
    u,v = u-1,v-1
    point[u].append(v)
    point[v].append(u)

uf = unionfind(N)
cnt = 0

for pos in range(N):
    cnt += 1
    for nv in point[pos]:
        if uf.same(pos,nv) == False:
            cnt -= 1
            uf.unit(pos,nv)
print(cnt)