# N の約数の個数をカウント
def divisors(N):
    num=0
    for i in range(1,N+1):
        if i*i>N:
            break
        if N%i!=0:
            continue

        num+=1
        if N//i!=i:
            num+=1

    return num


if __name__ =="__main__":
    N=int(input())
    # 約数の個数を管理
    table=[0 for _ in range(N)]
    for i in range(1,N):
        table[i]=divisors(i)

    ans=0
    # AB の値を全探索
    for i in range(1,N):
        ab=i
        cd=N-i
        ans+=table[ab]*table[cd]

    print(ans)