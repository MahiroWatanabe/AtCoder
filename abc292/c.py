'リスト形式で約数を全部表示'
def calc_divisors(N):
    res = []

    for i in range(1, N + 1):
        if i * i > N:
            break
        
        if N % i != 0:
            continue

        res.append(i)

        if N // i != i:
            res.append(N // i)

    res.sort()
    return res

N = int(input())
ans = 0

for i in range(1,N):
    ans += len(calc_divisors(i))*len(calc_divisors(N-i))
    
print(ans)