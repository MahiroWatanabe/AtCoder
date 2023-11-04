# べき乗の計算は誤差が出るので、pow関数では行わない
# 大きい数の計算は誤差が生まれるので、誤差を考えて実装を行う
B = int(input())
for i in range(20):
    tmp = i
    for j in range(i - 1):
        tmp *= i
    if tmp == B:
        print(i)
        exit()
print(-1)
