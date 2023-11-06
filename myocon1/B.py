A, B, W = map(int, input().split())
W_g = W * 1000
min_ans = 10**15
max_ans = -(10**15)

for i in range(1, 10**6 + 10):
    if A * i <= W_g <= B * i:
        min_ans = min(min_ans, i)
        max_ans = max(max_ans, i)

if min_ans == 10**15:
    print("UNSATISFIABLE")
else:
    print(min_ans, max_ans)
