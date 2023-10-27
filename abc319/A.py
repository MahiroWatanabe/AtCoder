N,M,P = map(int, input().split())
cnt = 0

while True:
    if M+P*cnt > N:
        print(cnt)
        break
    else:
        cnt += 1