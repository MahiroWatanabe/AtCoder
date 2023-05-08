N = int(input())
s = input()
if "|" in s[: s.index("*")] and "|" in s[s.index("*") + 1 :]:
    print("in")
else:
    print("out")
