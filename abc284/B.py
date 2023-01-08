T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    cnt = 0
    for i in A:
        if i%2 != 0:
            cnt += 1
    print(cnt)