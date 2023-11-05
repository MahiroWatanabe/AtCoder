X, Y = map(int, input().split())
if X < Y and Y - X <= 2:
    print("Yes")
elif X > Y and X - Y <= 3:
    print("Yes")
else:
    print("No")
