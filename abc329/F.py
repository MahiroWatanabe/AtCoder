cnt = [0] * 26


def solve(S):
    N = len(S)
    for c in S:
        cnt[ord(c) - ord("a")] += 1
    return f(N)


def f(l):
    if l == 0:
        return 1
    ret = 0
    for i in range(26):
        if cnt[i] >= l:
            ret += f(l - 1)
    return ret


N = int(input())
S = input()
print(solve(S))
