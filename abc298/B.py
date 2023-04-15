def is_possible(A, B):
    N = len(A)
    for _ in range(4):
        flag = True
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1 and B[i][j] != 1:
                    flag = False
                    break
            if not flag:
                break  
        if flag:
            return True            
        A = [[A[N-1-j][i] for j in range(N)] for i in range(N)]  # A を 90 度回転
    
    return False


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

print("Yes" if is_possible(A, B) else "No")
