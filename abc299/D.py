N = int(input())
left = 1
right = N
while right - left > 1:
    mid = (left + right) // 2
    print("?", mid)
    S = input()
    if S == "0":
        left = mid
    else:
        right = mid
print("!", left)
