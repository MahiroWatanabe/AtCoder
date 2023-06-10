class unionfind:
    def __init__(self, n):
        self.n=n
        self.parent_size=[-1]*n
        
    def merge(self, a, b):
        x, y=self.leader(a), self.leader(b)
        if x == y: return
        if abs(self.parent_size[x])<abs(self.parent_size[y]): x, y=y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return
    
    def same(self, a, b):
        return self.leader(a) == self.leader(b)
    
    def leader(self, a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    
    def size(self, a):
        return abs(self.parent_size[self.leader(a)])
    
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]
    
N,M = map(int, input().split())
uf = unionfind(N)
for _ in range(M):
    u,v = map(int, input().split())
    u,v = u-1,v-1
    if not uf.same(u,v):
        uf.merge(u,v)
        
K = int(input())
D = set()
for _ in range(K):
    x,y = map(int, input().split())
    x,y = x-1,y-1
    a,b = uf.leader(x),uf.leader(y)
    a,b = min(a,b),max(a,b)
    D.add((a,b))

Q = int(input())
for _ in range(Q):
    p,q = map(int, input().split())
    p,q = p-1,q-1
    a,b = uf.leader(p),uf.leader(q)
    a,b = min(a,b),max(a,b)
    
    if (a,b) in D:
        print("No")
    else:
        print("Yes")