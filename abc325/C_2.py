# unionfindを使った解法
# 二次元配列を一次元に変換
class unionfind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


H, W = map(int, input().split())
S = [input() for _ in range(H)]
XY = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
N = H * W
uf = unionfind(N)

for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            continue
        for dx, dy in XY:
            x = i + dx
            y = j + dy
            if 0 <= x < H and 0 <= y < W and S[x][y] == "#":
                uf.merge(i * W + j, x * W + y)
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            if uf.leader(i * W + j) == i * W + j:
                ans += 1

print(ans)
