S = input()
T = input()
m = len(T)
ans = [True for _ in range(m+1)]

for j in range(2):
    flag = True  
    for i in range(m):   
        if S[i] != T[i] and S[i] != "?" and T[i] != "?":
            flag = False
        if not flag:
            ans[i+1] = False
        
    S = S[::-1]
    T = T[::-1]
    ans = ans[::-1]

for i in range(m+1):
    if ans[i]:
        print("Yes")
    else:
        print("No")