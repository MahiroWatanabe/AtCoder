# 列に含まれる文字が一種類で個数が2以上
def toDelete(x):
    tot = 0
    k = 0
    for j in range(26):
        tot += x[j]
        if x[j]:
            k += 1
    return tot >= 2 and k == 1

def del_cookie(i, j):
    if row_deleted[i] or col_deleted[j]:
        return
    row[i][a[i][j]] -= 1
    col[j][a[i][j]] -= 1

h, w = map(int, input().split())
c = [input() for _ in range(h)]
# cはなんの文字か高速に判定
a = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        a[i][j] = ord(c[i][j]) - ord('a')

m = 26
row = [[0] * m for _ in range(h)]
col = [[0] * m for _ in range(w)]
row_deleted = [False] * h
col_deleted = [False] * w

for i in range(h):
    for j in range(w):
        row[i][a[i][j]] += 1
        col[j][a[i][j]] += 1

upd = True
while upd:
    upd = False
    del_row = []
    del_col = []

    for i in range(h):
        if row_deleted[i]:
            continue
        if toDelete(row[i]):
            del_row.append(i)

    for j in range(w):
        if col_deleted[j]:
            continue
        if toDelete(col[j]):
            del_col.append(j)

    for i in del_row:
        for j in range(w):
            del_cookie(i, j)
        row_deleted[i] = True
        upd = True

    for j in del_col:
        for i in range(h):
            del_cookie(i, j)
        col_deleted[j] = True
        upd = True

ans = 0
for i in range(h):
    for j in range(w):
        if not row_deleted[i] and not col_deleted[j]:
            ans += 1
print(row_deleted)
print(col_deleted)
print(ans)
