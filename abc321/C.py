# bit全探索　最大値の見積もりができていない
def f(bit):
    S = ""
    for i in range(len(e)):
        if (bit >> i) & 1:
            S += str(i)
            
    return int(S[::-1])

K = int(input())
D = []
e = "9876543210"
for bit in range(1,2**10):
    D.append(f(bit))

D.sort()
print(D[K])